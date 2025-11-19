# NiWrap developer and build tools

Aims to be both a shared Python API to iterate and fetch all the NiWrap data, as well as entrypoints to build/test/manage used by developers and automations (including CI).

## Usage

```sh
uv --directory tooling run wrap --help
```

```
usage: wrap [-h] {build,sync,test} ...

Niwrap developer and build tools.

options:
  -h, --help         show this help message and exit

commands:
  Available commands

  {build,sync,test}  Command help
    build            Build distributions
    sync             Synchronize metadata (i.e. build coverage tables for READMEs...)
    test             Run tests
```
