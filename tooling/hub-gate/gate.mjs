/**
 * Compiler-lockstep gate (Phase C / architecture A, N2).
 *
 * The hub no longer fetches prebuilt JSON Schema / a JS bundle; it bundles
 * `@styx-api/core` and compiles each hosted descriptor in the browser, one at a
 * time. The catalog build, by contrast, *skips* a tool it can't compile (a
 * warning, not a failure) - so a compiler regression that drops a tool would
 * sail through the build yet 500 that exact tool in the hub at runtime.
 *
 * This gate closes that gap: with the pinned `@styx-api/core` (the version the
 * hub bundles), it runs the hub's exact per-descriptor pipeline over every
 * descriptor in the built layout and fails if any single one errors. It also
 * asserts the manifest's recorded compiler version matches the installed one
 * (the C8 lockstep).
 *
 * Usage:  node gate.mjs [pagesDir]      (pagesDir defaults to ./dist/pages)
 */

import { readFileSync } from "node:fs";
import * as path from "node:path";

import {
  appEntrypoint,
  compile,
  createContext,
  defaultPipeline,
  generateOutputsSchema,
  generateSchema,
  generateTypeScript,
  resolveOutputs,
  solve,
} from "@styx-api/core";
import { transform } from "sucrase";
import * as styxdefs from "styxdefs";

const PROJECT = "niwrap";

// `@styx-api/core`'s `exports` map doesn't expose ./package.json, so read the
// installed version from this package's own node_modules.
const installedCoreVersion = JSON.parse(
  readFileSync(
    path.join(import.meta.dirname, "node_modules", "@styx-api", "core", "package.json"),
    "utf8",
  ),
).version;

const pagesDir = path.resolve(process.cwd(), process.argv[2] ?? "dist/pages");

function fail(message) {
  console.error(`✗ ${message}`);
  process.exit(1);
}

/**
 * Mirror of the hub worker's `buildExecute`: transpile the generated TypeScript
 * to CJS, evaluate it against the real `styxdefs`, and confirm the named execute
 * export exists. Catches generated-code syntax errors and a missing entrypoint
 * (which `generateTypeScript` - returning a string - cannot).
 */
function buildExecute(tsCode, executeName) {
  const { code } = transform(tsCode, { transforms: ["typescript", "imports"] });
  const module = { exports: {} };
  const requireShim = (name) => {
    if (name === "styxdefs") return styxdefs;
    throw new Error(`generated code required an unexpected module: ${name}`);
  };
  const factory = new Function("require", "module", "exports", code);
  factory(requireShim, module, module.exports);
  if (typeof module.exports[executeName] !== "function") {
    throw new Error(`generated module is missing the execute export "${executeName}"`);
  }
}

/** The hub's exact per-descriptor pipeline. Throws if any stage fails. */
function checkTool(descriptor, format, packageName, appName) {
  const parsed = compile(descriptor, { format, filename: appName });
  if (parsed.errors.length > 0) {
    throw new Error(`parse: ${parsed.errors.map((e) => e.message).join("; ")}`);
  }
  const piped = defaultPipeline.apply(parsed.expr);
  const solveResult = solve(piped.expr);
  const outputs = resolveOutputs(piped.expr, solveResult);
  const ctx = createContext(piped.expr, solveResult, outputs, {
    app: parsed.meta,
    package: { name: packageName },
    project: { name: PROJECT },
  });

  // Forms (H3): both schemas must generate.
  generateSchema(ctx);
  generateOutputsSchema(ctx);

  // Command/outputs (H4): entrypoint resolves and generated code transpiles+loads.
  const entry = appEntrypoint(ctx);
  if (!entry) throw new Error("no dispatch entrypoint (missing app id or package name)");
  buildExecute(generateTypeScript(ctx), entry.executeFn);
}

// --- Load the built layout -------------------------------------------------

const index = JSON.parse(readFileSync(path.join(pagesDir, "index.json"), "utf8"));
const release = index.versions.find((v) => v.version === index.latest);
if (!release) fail(`index.json: latest "${index.latest}" not found in versions`);

const catalogPath = path.join(pagesDir, release.catalog);
const catalog = JSON.parse(readFileSync(catalogPath, "utf8"));
const catalogDir = path.dirname(catalogPath);

// --- Lockstep: manifest version == the @styx-api/core we compile with --------

const manifestVersion = catalog.compiler?.version;
if (manifestVersion !== installedCoreVersion) {
  fail(
    `compiler lockstep violated: manifest pins @styx-api/core@${manifestVersion} ` +
      `but the gate installed @${installedCoreVersion}. Bump them together ` +
      `(wrap hub-build --compiler and tooling/hub-gate/package.json).`,
  );
}

// --- Compile every descriptor the way the hub will ---------------------------

console.log(
  `Gate: compiling every descriptor in ${catalog.project}@${catalog.version} ` +
    `with @styx-api/core@${installedCoreVersion}`,
);

let checked = 0;
const failures = [];

for (const pkg of catalog.packages) {
  for (const app of pkg.apps) {
    if (!app.descriptor) continue; // listed but unwrapped; the hub shows a CTA
    checked++;
    const id = `${pkg.name}/${app.name}`;
    try {
      const descriptor = readFileSync(path.join(catalogDir, app.descriptor), "utf8");
      checkTool(descriptor, app.format, pkg.name, app.name);
    } catch (err) {
      failures.push({ app: id, error: err instanceof Error ? err.message : String(err) });
    }
  }
}

if (failures.length > 0) {
  console.error(`\n✗ ${failures.length}/${checked} descriptors failed:`);
  for (const f of failures) console.error(`  - ${f.app}: ${f.error}`);
  process.exit(1);
}

console.log(`✓ all ${checked} descriptors compiled cleanly (forms + command codegen)`);
