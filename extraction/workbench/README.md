# Connectome Workbench metadata extraction

```sh
# Build the image
docker build -f workbench-dump.Dockerfile -t workbench-metadata .

# Extract all metadata files to your host
docker run --rm -v $(pwd)/metadata:/output workbench-metadata \
    bash -c "cp -r /app/metadata/* /output/"

# OR on Windows host: 
# docker run --rm -v %cd%/metadata:/output workbench-metadata bash -c "cp -r /app/metadata/* /output/"

# Copy metadata in the correct structure to ../../src/niwrap/workbench and app.json and version.json
python process_workbench_metadata.py
```