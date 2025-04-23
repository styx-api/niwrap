import glob
import json


def generate_value_key(input_id):
    return f"[{input_id.upper()}]"


# Find all JSON files in descriptors/*/
json_files = glob.glob("descriptors/*/*.json")

for json_filename in json_files:
    with open(json_filename, "r") as file:
        data = json.load(file)

    changes_made = False

    # Check for 'inputs' field in the JSON structure
    if "inputs" in data:
        for input_item in data["inputs"]:
            if ("value-key" not in input_item) or (input_item["value-key"] == ""):
                if "id" in input_item:
                    new_value_key = generate_value_key(input_item["id"])
                    input_item["value-key"] = new_value_key
                    changes_made = True
                    print(
                        f"Added value-key '{new_value_key}' for input with id '{input_item['id']}' in {json_filename}"
                    )
                else:
                    print(
                        f"Warning: Input is missing both 'value-key' and 'id' fields: {input_item} in {json_filename}"
                    )

    # Write back changes to the file if any value-keys were added
    if changes_made:
        with open(json_filename, "w") as file:
            json.dump(data, file, indent=2)
        print(f"Updated {json_filename} with new value-keys.")
