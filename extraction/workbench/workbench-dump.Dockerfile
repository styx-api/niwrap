FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

# Install all required dependencies (proven to work)
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

WORKDIR /workspace

# Copy source
COPY source/ /workspace/source/

# Fix .git issue and Qt compatibility
RUN rm -f /workspace/source/.git && \
    sed -i 's/#include <QtEnvironmentVariables>/#include <QProcessEnvironment>/' \
        /workspace/source/src/Common/WorkbenchInstallationAssistant.cxx

# Build wb_command
WORKDIR /workspace/source/build
RUN cmake -D CMAKE_BUILD_TYPE=Release \
          -D WORKBENCH_MESA_DIR=/usr \
          -D WORKBENCH_USE_QT5=TRUE \
          ../src && \
    make -j16 wb_command

# Verify build succeeded
RUN test -f CommandLine/wb_command && \
    echo "wb_command built successfully!"

# Extract metadata for all commands
RUN mkdir -p /workspace/metadata && \
    echo "===== Discovering all wb_command subcommands =====" && \
    ./CommandLine/wb_command -list-commands | awk '{print $1}' > /workspace/metadata/all_commands.txt && \
    echo "Found $(wc -l < /workspace/metadata/all_commands.txt) commands"

# Process each command to extract its metadata
RUN cd /workspace/source/build && \
    total=$(wc -l < /workspace/metadata/all_commands.txt) && \
    count=0 && \
    while IFS= read -r cmd; do \
        count=$((count + 1)); \
        clean_name=${cmd#-}; \
        echo "[$count/$total] Extracting metadata for: $cmd"; \
        ./CommandLine/wb_command "$cmd" > "/workspace/metadata/${clean_name}.json" 2>&1 || true; \
    done < /workspace/metadata/all_commands.txt && \
    echo "Metadata extraction complete!"

# Copy to final locations
RUN mkdir -p /app/bin /app/metadata && \
    cp /workspace/source/build/CommandLine/wb_command /app/bin/ && \
    cp -r /workspace/metadata/* /app/metadata/ && \
    echo "Total metadata files: $(ls -1 /app/metadata/*.json | wc -l)"

# Clean up build artifacts to reduce image size
RUN rm -rf /workspace/source/build

ENV PATH="/app/bin:${PATH}"
WORKDIR /app

# Add convenience script for re-extraction if needed
RUN cat > /app/extract_all.sh << 'EOF'
#!/bin/bash
echo "Extracting metadata for all wb_command subcommands..."
wb_command -list-commands | awk '{print $1}' | while read cmd; do
    clean=${cmd#-}
    echo "Processing: $cmd"
    wb_command "$cmd" > "/app/metadata/${clean}.json" 2>&1
done
echo "Done!"
EOF

RUN chmod +x /app/extract_all.sh

CMD ["bash"]