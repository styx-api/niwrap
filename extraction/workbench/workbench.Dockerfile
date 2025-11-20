FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

# Install runtime dependencies and build tools
RUN apt-get update && apt-get install -y \
    # Build essentials
    build-essential \
    cmake \
    git \
    make \
    g++ \
    # Qt5 components
    qtbase5-dev \
    qt5-qmake \
    qttools5-dev \
    qttools5-dev-tools \
    libqt5opengl5-dev \
    libqt5svg5-dev \
    libqt5xmlpatterns5-dev \
    libqt5concurrent5 \
    libqt5core5a \
    libqt5gui5 \
    libqt5network5 \
    libqt5widgets5 \
    libqt5xml5 \
    # OpenGL and Mesa
    libosmesa6-dev \
    mesa-common-dev \
    libgl1-mesa-dev \
    libglu1-mesa-dev \
    libglew-dev \
    # Math and scientific libraries
    liblapack-dev \
    libblas-dev \
    # Compression
    zlib1g-dev \
    libbz2-dev \
    # SSL/Crypto
    libssl-dev \
    # XML
    libxml2-dev \
    libxml2 \
    # Fonts and rendering
    libfreetype6-dev \
    libfontconfig1-dev \
    libglib2.0-dev \
    # System libraries
    libxkbcommon-dev \
    libxkbcommon-x11-dev \
    libx11-dev \
    libxext-dev \
    libxfixes-dev \
    libxi-dev \
    libxrender-dev \
    libxcb1-dev \
    libx11-xcb-dev \
    libxcb-glx0-dev \
    # OpenMP
    libgomp1 \
    libomp-dev \
    # Tools
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Set Workbench version
ARG WORKBENCH_VERSION=v2.1.0
ENV WORKBENCH_VERSION=${WORKBENCH_VERSION}

WORKDIR /tmp/build

# Clone specific version from GitHub
RUN git clone --depth 1 --branch ${WORKBENCH_VERSION} \
    https://github.com/Washington-University/workbench.git

# Fix Qt compatibility
RUN sed -i 's/#include <QtEnvironmentVariables>/#include <QProcessEnvironment>/' \
        /tmp/build/workbench/src/Common/WorkbenchInstallationAssistant.cxx

# Build Workbench
WORKDIR /tmp/build/workbench-build
RUN cmake -D CMAKE_BUILD_TYPE=Release \
          -D WORKBENCH_MESA_DIR=/usr \
          -D WORKBENCH_USE_QT5=TRUE \
          -D CMAKE_INSTALL_PREFIX=/app \
          ../workbench/src && \
    make -j$(nproc) && \
    make install

# Verify installation
RUN /app/bin/wb_command -version

# Clean up build artifacts
RUN rm -rf /tmp/build

# Add to PATH
ENV PATH="/app/bin:${PATH}"

WORKDIR /data

# Set metadata
LABEL org.opencontainers.image.title="Connectome Workbench"
LABEL org.opencontainers.image.description="Connectome Workbench command-line tools"
LABEL org.opencontainers.image.version="${WORKBENCH_VERSION}"
LABEL org.opencontainers.image.source="https://github.com/Washington-University/workbench"

CMD ["wb_command", "-version"]