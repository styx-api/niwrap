# hub-embed

Precomputed semantic-search embeddings for the niwrap.dev hub.

Both the web hub and `niwrap-mcp` want capability/synonym search ("bias field
correction" → `ants/N4BiasFieldCorrection`) over the catalog. Embedding every
tool is the expensive, cacheable half and is a pure function of one
`catalog.json` — so it's precomputed here in CI and **published to Pages as a
peer of the catalog**, versioned with it. Only the query is embedded live,
client-side, by the same model. See
[`niwrap-mcp/docs/embeddings-contract.md`](https://github.com/childmindresearch/niwrap-mcp/blob/main/docs/embeddings-contract.md)
for the full artifact contract.

This step runs **after** `wrap hub-build`, over the same output tree. It reads
`index.json` → `latest` → `<version>/catalog.json`, embeds every callable tool
(apps with a `descriptor`) once in catalog order, and writes into the version
directory:

```
<version>/embeddings.f32        row-major float32, count*dim*4 bytes
<version>/embeddings.meta.json  model, dim, encoding, version, count, tools[]
```

then patches that version's entry in `index.json` with the `embeddings` announce
object. Row `i` of the blob is `meta.tools[i]`. Vectors are mean-pooled and
L2-normalized, so cosine similarity is a plain dot product.

These are CI build artifacts — they live in the Pages output next to
`catalog.json`, **not** committed to the repo.

## Fidelity — build with the model the clients query with

The indexed vectors and the live query vector must share one embedding space, so
the index is built with the **same ONNX artifact** the clients load:
`Xenova/all-MiniLM-L6-v2` via `@huggingface/transformers` (transformers.js /
ONNX Runtime) — **not** the PyTorch `sentence-transformers` original, whose
outputs drift enough to degrade cosine ranking. The embed call (mean pooling,
normalize) is identical to `niwrap-mcp`'s `embed()`, and the indexed text +
ordering are ported verbatim from `niwrap-mcp/scripts/build-embeddings.ts`:

```
tool_id = "<package>/<app.name>"
text    = `${pkg} ${app}` + (description ? `: ${description}` : "")
```

Changing the model is a breaking change: it requires rebuilding every published
version's index and a coordinated client update.

## Run

```bash
# from the niwrap repo root
uv --directory tooling run wrap hub-build --out dist/pages
npm --prefix tooling/hub-embed ci
node tooling/hub-embed/build-embeddings.mjs dist/pages
```

First run downloads the ONNX model from the HF Hub into the transformers.js
cache; CI caches that between runs. The step fails the build if the model can't
be loaded or the output fails validation (`bytes == count*dim*4`).

## Scope

Only the `latest` version is embedded. Older versions stay embedding-less and
clients fall back to lexical search — the existing default when the `embeddings`
field is absent from `index.json`. Only the `f32` encoding is shipped today
(`int8` is reserved in the contract).
