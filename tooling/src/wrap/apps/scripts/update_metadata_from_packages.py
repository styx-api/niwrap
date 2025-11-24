import glob
import json
import os


def load_package_data(package_id):
    package_file = f"packages/{package_id}.json"
    if os.path.exists(package_file):
        with open(package_file, "r") as file:
            return json.load(file)
    return None


# Find all JSON files in descriptors/*/
json_files = glob.glob("descriptors/*/*.json")

for json_filename in json_files:
    with open(json_filename, "r") as file:
        descriptor = json.load(file)

    changes_made = False

    # Extract package_id from the descriptor filename
    package_id = os.path.basename(os.path.dirname(json_filename))

    # Load package data
    package_data = load_package_data(package_id)

    if package_data:
        # Update descriptor fields
        if descriptor.get("author") != package_data.get("author"):
            descriptor["author"] = package_data["author"]
            changes_made = True

        if descriptor.get("url") != package_data.get("url"):
            descriptor["url"] = package_data["url"]
            changes_made = True

        if descriptor.get("tool-version") != package_data.get("version"):
            descriptor["tool-version"] = package_data["version"]
            changes_made = True

        container_image = {"type": "docker", "image": package_data["container"]}
        if descriptor.get("container-image") != container_image:
            descriptor["container-image"] = container_image
            changes_made = True

        # Write back changes to the file if any updates were made
        if changes_made:
            with open(json_filename, "w") as file:
                json.dump(descriptor, file, indent=2)
                file.write("\n")
            print(f"Updated {json_filename} with package data.")
    else:
        print(f"Warning: No package data found for {package_id}")
