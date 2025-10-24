import glob
import json
import re

out_regex = re.compile(r"\b(?:\w*_)?(?:output|out)(?:_\w*)?\b", re.IGNORECASE)


def find_fix_outputs(data: dict[str, str], json_file: str) -> bool:
    if "inputs" not in data:
        return False

    outputs = {
        re.split(r"\]", output["path-template"])[0] + "]"
        for output in data.get("output-files", [])
    }

    changes_made = False
    for input_obj in data["inputs"]:
        if not all(key in input_obj for key in ("id", "type")):
            print(f"Warning: missing 'name' and / or 'type' in {json_file}")
            continue

        if (
            out_regex.search(input_obj["id"])
            and input_obj["type"] == "File"
            and input_obj["value-key"] in outputs
        ):
            input_obj["type"] = "String"
            changes_made = True
            print(f"Changed type to 'String' for {input_obj['name']} in {json_file}")

        # Check nested structures recursively
        if isinstance(input_obj["type"], dict):
            changes_made |= find_fix_outputs(
                data=input_obj["type"], json_file=json_file
            )
        elif isinstance(input_obj["type"], list):
            for obj in input_obj["type"]:
                if isinstance(obj, dict):
                    changes_made |= find_fix_outputs(data=obj, json_file=json_file)

    return changes_made


# Path to folder with JSON descriptors
json_files = glob.glob("descriptors/*/*.json")

for json_file in json_files:
    with open(json_file, "r") as f:
        data = json.load(f)

    changes_made = find_fix_outputs(data=data, json_file=json_file)

    if changes_made:
        with open(json_file, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Updated {json_file} output argument types.")
