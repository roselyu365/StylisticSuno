#!/usr/bin/env python3
"""
Data Management Tool for SonicPalette
Use this script to easily add, modify, and view data entries
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any

DATA_DIR = Path("data")

def load_data(file: str) -> Dict:
    """Load JSON data file"""
    filepath = DATA_DIR / file
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {file} not found")
        return {}
    except Exception as e:
        print(f"Error loading {file}: {e}")
        return {}

def save_data(file: str, data: Dict):
    """Save data to JSON file"""
    filepath = DATA_DIR / file
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"✓ Saved to {filepath}")

def add_emotion(name: str, keywords: list, description: str):
    """Add a new emotion"""
    data = load_data("emotions.json")
    data[name] = {
        "keywords": keywords,
        "description": description
    }
    save_data("emotions.json", data)
    print(f"✓ Added emotion: {name}")

def add_style(name: str, config: Dict):
    """Add a new musical style"""
    data = load_data("styles.json")
    data[name] = config
    save_data("styles.json", data)
    print(f"✓ Added style: {name}")

def add_reference(style: str, artist: str, title: str, note: str):
    """Add a reference track"""
    data = load_data("references.json")
    if style not in data:
        data[style] = []
    data[style].append([f"{artist} - {title}", note])
    save_data("references.json", data)
    print(f"✓ Added reference: {artist} - {title}")

def list_emotions():
    """List all emotions"""
    data = load_data("emotions.json")
    print("\n=== Emotions ===")
    for name, info in data.items():
        print(f"  {name}: {info.get('description', 'N/A')}")
        print(f"    Keywords: {', '.join(info.get('keywords', []))}")
        print()

def list_styles():
    """List all musical styles"""
    data = load_data("styles.json")
    print("\n=== Musical Styles ===")
    for name, info in data.items():
        print(f"  {name}")
        print(f"    BPM: {info.get('bpm_min')}-{info.get('bpm_max')}")
        print(f"    Keywords: {', '.join(info.get('keywords', [])[:5])}")
        print()

def interactive_add_style():
    """Interactive style addition"""
    print("\n=== Add New Musical Style ===")
    name = input("Style name: ").strip()
    
    keywords_input = input("Keywords (comma-separated): ").strip()
    keywords = [k.strip() for k in keywords_input.split(",")]
    
    bpm_min = int(input("BPM min: ").strip())
    bpm_max = int(input("BPM max: ").strip())
    
    instruments_input = input("Instruments (comma-separated): ").strip()
    instruments = [i.strip() for i in instruments_input.split(",")]
    
    description = input("Description: ").strip()
    
    # Ask for chord progressions
    chords = []
    print("\nAdd chord progressions (press Enter to skip):")
    while True:
        roman = input("Roman numerals: ").strip()
        if not roman:
            break
        c_example = input("C example: ").strip()
        chords.append({"roman": roman, "C": c_example})
    
    new_style = {
        "keywords": keywords,
        "bpm_min": bpm_min,
        "bpm_max": bpm_max,
        "instruments": instruments,
        "chords": chords,
        "description": description
    }
    
    add_style(name, new_style)

def main():
    if len(sys.argv) < 2:
        print("""
Usage: python manage_data.py <command> [args]

Commands:
  list-emotions       List all emotions
  list-styles         List all musical styles
  add-style           Interactive style addition
  add-emotion         Add new emotion (interactive)
  add-reference       Add reference track (interactive)
  view <file>            View JSON file (emotions, styles, references, emotion_to_styles)
""")
        return
    
    command = sys.argv[1]
    
    if command == "list-emotions":
        list_emotions()
    elif command == "list-styles":
        list_styles()
    elif command == "add-style":
        interactive_add_style()
    elif command == "view":
        if len(sys.argv) < 3:
            print("Usage: python manage_data.py view <filename>")
            return
        filename = sys.argv[2]
        data = load_data(filename)
        print(f"\n=== {filename} ===")
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()

