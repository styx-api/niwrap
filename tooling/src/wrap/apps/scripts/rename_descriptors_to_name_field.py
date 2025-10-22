import glob
import json
import os

# Path to the folder with JSON descriptors
json_files = glob.glob("descriptors/*/*.json")

for json_file in json_files:
    with open(json_file, "r") as f:
        data = json.load(f)

    # Ensure the "name" field exists in the JSON
    if "name" in data:
        new_filename = data["name"] + ".json"
        new_filepath = os.path.join(os.path.dirname(json_file), new_filename)

        # Rename the file if the new name is different
        if json_file != new_filepath:
            os.rename(json_file, new_filepath)
            print(f"Renamed {json_file} to {new_filepath}")
    else:
        print(f'No "name" field in {json_file}')
