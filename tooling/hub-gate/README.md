# hub-gate

Compiler-lockstep gate for the niwrap.dev hub (Phase C / architecture A, N2).

The hub no longer ships prebuilt JSON Schema or a JS runtime bundle. It bundles
`@styx-api/core` and compiles each hosted descriptor **in the browser**, one at a
time. The catalog build (`wrap hub-build`, and the styx2 catalog compile) instead
*skips* a tool it can't compile - a warning, not a failure - so a compiler
regression that drops a tool would pass the build yet 500 that exact tool in the
hub at runtime.

This gate closes that gap. With the pinned `@styx-api/core` (the version the hub
bundles), it runs the hub's exact per-descriptor pipeline over every descriptor in
the built layout and **fails if any single one errors**:

```
compile -> defaultPipeline -> solve -> resolveOutputs -> createContext
        -> generateSchema + generateOutputsSchema        (forms, H3)
        -> appEntrypoint + generateTypeScript -> sucrase  (command/outputs, H4)
```

It also asserts that the manifest's recorded compiler version matches the version
installed here (the C8 lockstep), so the version a user sees in a snippet always
matches `pip install niwrap`.

## Run

```bash
# from the niwrap repo root
uv --directory tooling run wrap hub-build --out dist/pages
npm --prefix tooling/hub-gate ci
node tooling/hub-gate/gate.mjs dist/pages
```

## Keeping it in lockstep

Three pins must move together when adopting a newer compiler:

1. `tooling/hub-gate/package.json` - `@styx-api/core` (what this gate compiles with).
2. `wrap hub-build --compiler` default (recorded in `catalog.json`).
3. The hub's bundled `@styx-api/core` (enforced hub-side, H6).

The gate fails loudly if (1) and (2) disagree.
