# syntax=docker/dockerfile:1
#
# Reproducible MRtrix3 command-metadata dumper.
#
# Builds MRtrix3 from an *official* version tag, applies two small metadata
# patches, and dumps every command's interface as JSON. The dump is the build
# artifact: export it straight to the host with BuildKit's local output.
#
#   docker buildx build \
#     --build-arg MRTRIX_VERSION=3.0.4 \
#     --target artifact \
#     --output type=local,dest=dump/3.0.4 \
#     extraction/mrtrix
#
# Bump versions in versions.json and run extract.sh / extract.ps1 to drive a
# whole matrix. See README.md.

ARG MRTRIX_VERSION=3.0.4

# --------------------------------------------------------------------------- #
# Stage 1 — build MRtrix3 from the official tag + our two metadata patches.    #
# --------------------------------------------------------------------------- #
# Base image digest-pinned for reproducibility (ubuntu:22.04 at the 3.0.4 build).
FROM ubuntu:22.04@sha256:4f838adc7181d9039ac795a7d0aba05a9bd9ecd480d294483169c5def983b64d AS builder
ARG MRTRIX_VERSION
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential g++ git python3 python3-pip \
      libeigen3-dev zlib1g-dev pkg-config \
    && ln -sf /usr/bin/python3 /usr/bin/python \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt
RUN git clone --depth 1 --branch "${MRTRIX_VERSION}" \
      https://github.com/MRtrix3/mrtrix3.git

WORKDIR /opt/mrtrix3
COPY patches/ /tmp/patches/
# cpp-json-usage  : adds the `__print_usage_json__` hook to core/app.cpp
# python-argdump  : adds the `__print_argdump__` hook to lib/mrtrix3/app.py
# --recount keeps the hand-written python hunk robust to minor line drift.
RUN git apply --recount --verbose /tmp/patches/cpp-json-usage.patch \
 && git apply --recount --verbose /tmp/patches/python-argdump.patch \
 && git -c user.email=niwrap@styx-api.org -c user.name=niwrap commit -aqm "niwrap metadata patches" \
 && git tag -f "${MRTRIX_VERSION}"
# Commit the patches and re-point the tag at the result so MRtrix's build sees a
# clean tag — otherwise `git describe --dirty` bakes a "<version>-dirty" string
# into every dumped descriptor's version field.

# Headless build — we only need command metadata, not the Qt GUI commands
# (mrview, shview), so -nogui keeps the image small and the build fast.
RUN ./configure -nogui && ./build

# --------------------------------------------------------------------------- #
# Stage 2 — dump every command's interface to /dump/{cpp,python}.             #
# --------------------------------------------------------------------------- #
FROM builder AS dump
ARG MRTRIX_VERSION
# argdump pinned for reproducibility. Plain `pip3 install` works because
# ubuntu:22.04 ships pip < PEP 668; on a newer base add --break-system-packages.
RUN pip3 install --no-cache-dir argdump==0.1.2
ENV PATH="/opt/mrtrix3/bin:${PATH}"
WORKDIR /opt/mrtrix3

RUN mkdir -p /dump/cpp /dump/python && echo "${MRTRIX_VERSION}" > /dump/VERSION && \
    echo "===== C++ commands (__print_usage_json__) =====" && \
    for f in cmd/*.cpp; do \
      n="$(basename "$f" .cpp)"; \
      if "$n" __print_usage_json__ > "/dump/cpp/$n.json" 2>/dev/null; then \
        echo "  ok   $n"; \
      else \
        echo "  skip $n (not built / no json hook)"; rm -f "/dump/cpp/$n.json"; \
      fi; \
    done && \
    echo "===== Python commands (__print_argdump__) =====" && \
    for f in $(grep -rlI "import mrtrix3" bin/); do \
      n="$(basename "$f")"; \
      if "$n" __print_argdump__ > "/dump/python/$n.json" 2>/dev/null; then \
        echo "  ok   $n"; \
      else \
        echo "  skip $n (argdump failed)"; rm -f "/dump/python/$n.json"; \
      fi; \
    done && \
    echo "C++:    $(ls -1 /dump/cpp    | wc -l) commands" && \
    echo "Python: $(ls -1 /dump/python | wc -l) commands"

# --------------------------------------------------------------------------- #
# Stage 3 — the dump IS the deliverable. `--target artifact --output          #
# type=local,dest=...` writes /dump/{cpp,python,VERSION} straight to the host. #
# --------------------------------------------------------------------------- #
FROM scratch AS artifact
COPY --from=dump /dump/ /
