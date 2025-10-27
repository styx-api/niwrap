#!/usr/bin/env python3
"""
Process Connectome Workbench metadata JSON files and organize them into the niwrap directory structure.
"""

import json
import os
import shutil
from pathlib import Path
from typing import Any


def is_valid_json_file(filepath: Path) -> bool:
    """Check if file starts with '{' indicating it's likely valid JSON."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            first_char = f.read(1)
            return first_char == '{'
    except Exception:
        return False


def load_json(filepath: Path) -> dict[str, Any]:
    """Load and parse a JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(data: dict[str, Any], filepath: Path, indent: int = 2) -> None:
    """Save data as formatted JSON to file."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent)


def extract_version_from_metadata(metadata: dict[str, Any]) -> str:
    """Extract version from the metadata's version_info field."""
    version_info = metadata.get('version_info', [])
    for line in version_info:
        if line.startswith('Version:'):
            return line.split(':', 1)[1].strip()
    # Fallback to default version if not found
    return "1.5.0"


def extract_command_name(metadata: dict[str, Any]) -> str:
    """Extract the command name from metadata."""
    command = metadata.get('command', '')
    # Remove leading dash if present
    if command.startswith('-'):
        return command[1:]
    return command


def create_app_json(metadata: dict[str, Any]) -> dict[str, Any]:
    """Create app.json structure from metadata."""
    command_name = extract_command_name(metadata)
    
    # Get description from help_text and short_description
    short_desc = metadata.get('short_description', '').strip()
    help_text = metadata.get('help_text', '').strip()
    
    # Format description: short description as first line, then help text
    description_parts = []
    if short_desc:
        # Convert to sentence case and ensure it ends with a period
        short_desc_formatted = short_desc[0].upper() + short_desc[1:].lower()
        if not short_desc_formatted.endswith('.'):
            short_desc_formatted += '.'
        description_parts.append(short_desc_formatted)
    
    if help_text:
        description_parts.append(help_text)
    
    description = '\n\n'.join(description_parts) if description_parts else ''
    
    return {
        "name": command_name,
        "source": {
            "type": "mrtrix",
            "path": "mrtrix.json"
        },
        "exe": "wb_command",
        "args": [
            metadata.get('command', f'-{command_name}')
        ],
        "docs": {
            "description": description
        }
    }


def create_version_json(version: str) -> dict[str, Any]:
    """Create version.json structure."""
    return {
        "name": version,
        "apps": []  # This will be populated with all app names for this version
    }


def main():
    # Setup paths
    metadata_dir = Path('metadata')
    output_base = Path('../../src/niwrap/workbench').resolve()  # Use absolute path
    
    # Check that metadata directory exists
    if not metadata_dir.exists():
        print(f"Error: metadata directory '{metadata_dir}' does not exist")
        return 1
    
    # Assert that the output base directory exists
    if not output_base.exists():
        print(f"Error: Output directory '{output_base}' does not exist")
        print("Please create it first: mkdir -p ../../src/niwrap/workbench")
        return 1
    
    # Track versions and their apps for version.json files
    versions_apps: dict[str, list] = {}
    
    # Process all JSON files in metadata directory
    json_files = list(metadata_dir.glob('*.json'))
    print(f"Found {len(json_files)} JSON files in metadata/")
    
    processed_count = 0
    skipped_count = 0
    
    for json_file in json_files:
        # Check if file starts with '{'
        if not is_valid_json_file(json_file):
            print(f"Skipping {json_file.name}: Does not start with '{{'")
            skipped_count += 1
            continue
        
        try:
            # Load the metadata
            metadata = load_json(json_file)
            
            # Extract version and command name
            version = extract_version_from_metadata(metadata)
            command_name = extract_command_name(metadata)
            
            if not command_name:
                print(f"Warning: No command name found in {json_file.name}, skipping")
                skipped_count += 1
                continue
            
            # Create output directory
            app_dir = output_base / version / command_name
            app_dir.mkdir(parents=True, exist_ok=True)
            
            # Copy the original metadata file as mrtrix.json
            dest_metadata = app_dir / 'mrtrix.json'
            shutil.copy2(json_file, dest_metadata)
            
            # Try to get relative path for display, but use name if it fails
            try:
                display_path = dest_metadata.relative_to(Path.cwd())
            except ValueError:
                display_path = f"{version}/{command_name}/mrtrix.json"
            print(f"Copied {json_file.name} -> {display_path}")
            
            # Create and save app.json
            app_json = create_app_json(metadata)
            app_json_path = app_dir / 'app.json'
            save_json(app_json, app_json_path)
            
            # Try to get relative path for display, but use name if it fails
            try:
                display_path = app_json_path.relative_to(Path.cwd())
            except ValueError:
                display_path = f"{version}/{command_name}/app.json"
            print(f"Created {display_path}")
            
            # Track this app for the version.json
            if version not in versions_apps:
                versions_apps[version] = []
            versions_apps[version].append(command_name)
            
            processed_count += 1
            
        except json.JSONDecodeError as e:
            print(f"Error: Failed to parse {json_file.name}: {e}")
            skipped_count += 1
        except Exception as e:
            print(f"Error processing {json_file.name}: {e}")
            skipped_count += 1
    
    # Create version.json files for each version
    for version, apps in versions_apps.items():
        version_dir = output_base / version
        version_json = create_version_json(version)
        version_json['apps'] = sorted(apps)  # Sort apps alphabetically
        version_json_path = version_dir / 'version.json'
        save_json(version_json, version_json_path)
        
        # Try to get relative path for display, but use name if it fails
        try:
            display_path = version_json_path.relative_to(Path.cwd())
        except ValueError:
            display_path = f"{version}/version.json"
        print(f"\nCreated {display_path} with {len(apps)} apps")
    
    # Summary
    print(f"\n{'='*50}")
    print(f"Processing complete!")
    print(f"  Processed: {processed_count} files")
    print(f"  Skipped: {skipped_count} files")
    print(f"  Versions created: {len(versions_apps)}")
    
    return 0


if __name__ == "__main__":
    exit(main())