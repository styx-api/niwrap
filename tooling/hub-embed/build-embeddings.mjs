/**
 * Precompute the hub's semantic-search index and publish it into the Pages tree.
 *
 * `wrap hub-build` (Python) writes the version-first layout — index.json plus
 * <version>/catalog.json + descriptors. This step runs *after* it, over that same
 * output tree: it embeds every callable tool once and writes the vectors next to
 * the catalog, then announces them in index.json. Both the web hub and
 * niwrap-mcp consume the result; only the live query is embedded client-side.
 *
 * Fidelity is the whole point (see docs/embeddings-contract.md): the index MUST
 * be built with the SAME ONNX artifact the clients query with —
 * `Xenova/all-MiniLM-L6-v2` via @huggingface/transformers (transformers.js /
 * ONNX Runtime), mean-pooled + L2-normalized — NOT the PyTorch
 * sentence-transformers original, whose outputs drift enough to degrade cosine
 * ranking. This is exactly niwrap-mcp's `embed()`.
 *
 * The indexed text and ordering are ported verbatim from
 * niwrap-mcp/scripts/build-embeddings.ts so an index built here is
 * interchangeable with one the reference would have produced.
 *
 * Writes (into <pagesDir>, which maps to niwrap.dev/niwrap/ when published):
 *   <version>/embeddings.f32        row-major float32, count*dim*4 bytes
 *   <version>/embeddings.meta.json  model, dim, encoding, version, count, tools[]
 * and patches index.json's <latest> entry with the `embeddings` announce object.
 *
 * Usage:  node build-embeddings.mjs [pagesDir]      (defaults to ./dist/pages)
 *
 * Today only the `latest` version is embedded; older versions stay
 * embedding-less and clients fall back to lexical search (the existing default).
 */

import { readFileSync, writeFileSync } from "node:fs";
import * as path from "node:path";

import { env as hfEnv, pipeline } from "@huggingface/transformers";

// The matched-pair invariant: same id the clients load to embed the query.
const EMBED_MODEL = "Xenova/all-MiniLM-L6-v2";
const EMBED_DIM = 384;
const ENCODING = "f32";
const BATCH = 64;

// transformers.js v4 is NOT configurable via env vars (no TRANSFORMERS_CACHE /
// HF_HOME); it reads `env.cacheDir`, defaulting to a dir *inside* node_modules.
// That's wiped by `npm ci` and so can't be cached across CI runs — so pin the
// model cache next to this package (outside node_modules) where actions/cache
// can persist it. import.meta.dirname keeps it stable regardless of cwd.
hfEnv.cacheDir = path.join(import.meta.dirname, ".cache");

const pagesDir = path.resolve(process.cwd(), process.argv[2] ?? "dist/pages");

/** @returns {never} - exits the process; never returns to the caller. */
function fail(message) {
  console.error(`✗ ${message}`);
  process.exit(1);
}

// --- Resolve the latest version's catalog from the built tree ----------------

const indexPath = path.join(pagesDir, "index.json");
const index = JSON.parse(readFileSync(indexPath, "utf8"));
const entry = index.versions?.find((v) => v.version === index.latest);
if (!entry) fail(`index.json: latest "${index.latest}" not found in versions`);

const version = entry.version;
const versionDir = path.join(pagesDir, version);
const catalog = JSON.parse(
  readFileSync(path.join(pagesDir, entry.catalog), "utf8"),
);
if (catalog.version !== version) {
  fail(
    `matched-pair binding violated: index latest is "${version}" but ` +
      `${entry.catalog} is version "${catalog.version}"`,
  );
}

// --- Collect callable tools + index text (verbatim from the reference) -------

const tools = [];
const texts = [];
for (const pkg of catalog.packages) {
  for (const app of pkg.apps) {
    if (!app.descriptor) continue; // only callable tools
    tools.push({
      tool_id: `${pkg.name}/${app.name}`,
      name: app.name,
      package: pkg.name,
      description: app.description,
    });
    texts.push(
      `${pkg.name} ${app.name}${app.description ? `: ${app.description}` : ""}`,
    );
  }
}

if (tools.length === 0) {
  fail(`no callable tools (apps with a descriptor) found in ${entry.catalog}`);
}

// --- Embed: mean-pool + L2-normalize via the ONNX model ----------------------

console.log(
  `Embedding ${tools.length} tools (catalog ${version}) with ${EMBED_MODEL} …`,
);

let extractor;
try {
  extractor = await pipeline("feature-extraction", EMBED_MODEL);
} catch (err) {
  fail(
    `could not load embedding model ${EMBED_MODEL}: ` +
      `${err instanceof Error ? err.message : String(err)}`,
  );
}

/** Embed texts into L2-normalized mean-pooled vectors (== niwrap-mcp embed()). */
async function embed(batch) {
  const out = await extractor(batch, { pooling: "mean", normalize: true });
  return out.tolist();
}

const all = new Float32Array(tools.length * EMBED_DIM);
for (let i = 0; i < texts.length; i += BATCH) {
  const vecs = await embed(texts.slice(i, i + BATCH));
  for (let k = 0; k < vecs.length; k++) {
    if (vecs[k].length !== EMBED_DIM) {
      fail(`model returned dim ${vecs[k].length}, expected ${EMBED_DIM}`);
    }
    all.set(vecs[k], (i + k) * EMBED_DIM);
  }
  process.stderr.write(`\r  ${Math.min(i + BATCH, texts.length)}/${texts.length}`);
}
process.stderr.write("\n");

// --- Write the vector blob + meta into the version directory -----------------

const bytes = all.byteLength;
const expectedBytes = tools.length * EMBED_DIM * 4;
if (bytes !== expectedBytes) {
  fail(`blob is ${bytes} bytes, expected count*dim*4 = ${expectedBytes}`);
}

const metaName = "embeddings.meta.json";
const vectorsName = "embeddings.f32";

const meta = {
  model: EMBED_MODEL,
  dim: EMBED_DIM,
  encoding: ENCODING,
  version, // == catalog version (matched-pair binding)
  count: tools.length,
  tools,
};
writeFileSync(path.join(versionDir, metaName), JSON.stringify(meta));
writeFileSync(path.join(versionDir, vectorsName), Buffer.from(all.buffer));

// --- Announce in index.json so clients can pre-flight before fetching --------

entry.embeddings = {
  model: EMBED_MODEL,
  dim: EMBED_DIM,
  count: tools.length,
  variants: [
    {
      encoding: ENCODING,
      meta: `${version}/${metaName}`,
      vectors: `${version}/${vectorsName}`,
      bytes,
    },
  ],
};
writeFileSync(indexPath, JSON.stringify(index, null, 2) + "\n");

console.log(
  `✓ wrote ${version}/${metaName} (${tools.length} tools) + ` +
    `${version}/${vectorsName} (${(bytes / 1e6).toFixed(1)} MB) ` +
    `and announced embeddings in index.json`,
);

// --- Sanity: a couple of capability queries should rank sensibly -------------

/** Cosine (== dot, both normalized) of a query against every indexed tool. */
async function topMatches(query, k = 5) {
  const [qv] = await embed([query]);
  if (qv.length !== EMBED_DIM) fail(`query embedded to dim ${qv.length}, expected ${EMBED_DIM}`);
  const scored = tools.map((t, i) => {
    const off = i * EMBED_DIM;
    let dot = 0;
    for (let j = 0; j < EMBED_DIM; j++) dot += qv[j] * all[off + j];
    return { tool_id: t.tool_id, score: dot };
  });
  scored.sort((a, b) => b.score - a.score);
  return scored.slice(0, k);
}

const SPOT_CHECKS = [
  { query: "skull strip", expect: "fsl/bet" },
  { query: "bias field correction", expect: "ants/N4BiasFieldCorrection" },
];

console.log("Spot-check ranking:");
for (const { query, expect } of SPOT_CHECKS) {
  const top = await topMatches(query);
  const rank = top.findIndex((t) => t.tool_id === expect);
  const where = rank >= 0 ? `#${rank + 1}` : "not in top-5";
  const mark = rank >= 0 ? "✓" : "⚠";
  console.log(
    `  ${mark} "${query}" → expect ${expect} (${where}); ` +
      `top: ${top.map((t) => `${t.tool_id} ${t.score.toFixed(3)}`).join(", ")}`,
  );
}
