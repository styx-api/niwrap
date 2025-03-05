const esbuild = require('esbuild');
// const { nodeExternalsPlugin } = require('esbuild-node-externals');
const { execSync } = require('child_process');

// Build for ESM
esbuild.build({
  entryPoints: ['src/index.ts'],
  outfile: 'dist/index.esm.js',
  bundle: true,
  minify: true,
  platform: 'neutral',
  format: 'esm',
  sourcemap: true,
//   plugins: [nodeExternalsPlugin()],
  target: ['es2020']
}).catch(() => process.exit(1));

// Build for CommonJS
esbuild.build({
  entryPoints: ['src/index.ts'],
  outfile: 'dist/index.cjs.js',
  bundle: true,
  minify: true,
  platform: 'node',
  format: 'cjs',
  sourcemap: true,
//   plugins: [nodeExternalsPlugin()],
  target: ['es2020']
}).catch(() => process.exit(1));

// Generate type definitions
try {
  execSync('tsc --noCheck --emitDeclarationOnly --outDir dist/types', { 
    stdio: ['pipe', 'pipe', 'pipe'],
    encoding: 'utf-8' 
  });
  console.log('TypeScript declarations generated successfully');
} catch (error) {
  console.error('TypeScript compilation failed:');
  console.error(error)

  if (error.stdout) {
    console.error(error.stdout);
  }

  if (error.stderr) {
    console.error(error.stderr);
  }

  process.exit(1);
}
