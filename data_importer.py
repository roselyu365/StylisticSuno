#!/usr/bin/env python3
"""
Data Importer for SonicPalette
Fetches and imports data from external sources to expand the knowledge base
"""

import json
import requests
from pathlib import Path
from typing import Dict, List
import time

DATA_DIR = Path("data")

# ============================================================================
# Last.fm API Integration
# ============================================================================

def fetch_artist_top_tracks(artist_name: str, api_key: str = None) -> List[tuple]:
    """
    Fetch top tracks from Last.fm for an artist
    Returns: List of (artist - title, description) tuples
    """
    if not api_key:
        print("Warning: Last.fm API key not provided")
        return []
    
    try:
        url = "http://ws.audioscrobbler.com/2.0/"
        params = {
            "method": "artist.gettoptracks",
            "artist": artist_name,
            "api_key": api_key,
            "format": "json",
            "limit": 5
        }
        response = requests.get(url, params=params, timeout=5)
        data = response.json()
        
        if "toptracks" in data and "track" in data["toptracks"]:
            tracks = []
            for track in data["toptracks"]["track"][:3]:
                title = track.get("name", "Unknown")
                tracks.append((f"{artist_name} - {title}", f"from {artist_name}'s top tracks"))
            return tracks
    except Exception as e:
        print(f"Error fetching from Last.fm: {e}")
    
    return []

# ============================================================================
# Open Music Database APIs
# ============================================================================

def fetch_musicbrainz_releases(artist: str, style: str) -> List[str]:
    """Fetch release info from MusicBrainz"""
    try:
        url = "https://musicbrainz.org/ws/2/release-group"
        headers = {"User-Agent": "SonicPalette/1.0"}
        params = {
            "artist": artist,
            "type": "album",
            "limit": 5,
            "fmt": "json"
        }
        response = requests.get(url, params=params, headers=headers, timeout=5)
        data = response.json()
        
        albums = []
        if "release-groups" in data:
            for release in data["release-groups"][:3]:
                title = release.get("title", "Unknown")
                albums.append(f"{artist} - {title}")
        return albums
    except Exception as e:
        print(f"MusicBrainz fetch error: {e}")
    return []

# ============================================================================
# Discogs API Integration
# ============================================================================

def fetch_discogs_genre_releases(genre: str) -> List[tuple]:
    """Fetch releases from Discogs by genre"""
    # Note: Requires Discogs API key
    try:
        # This is a placeholder - actual implementation would use Discogs API
        # You can get API keys from https://www.discogs.com/developers
        print(f"Would fetch {genre} releases from Discogs")
        return []
    except Exception as e:
        print(f"Discogs fetch error: {e}")
    return []

# ============================================================================
# Data Expansion Functions
# ============================================================================

def expand_styles_from_seed_data():
    """Add more styles from seed data"""
    seed_styles = {
        "House": {
            "keywords": ["house", "4/4", "piano", "disco", "深house"],
            "bpm_min": 120,
            "bpm_max": 130,
            "instruments": ["Four-on-floor kick", "Bass", "Piano chords", "Strings", "Vocal chops"],
            "chords": [
                {"roman": "I – V – vi – IV", "C": "C – G – Am – F"}
            ],
            "description": "Classic house music with disco roots"
        },
        "EDM": {
            "keywords": ["edm", "dance", "festival", "drop", "build", "电子舞曲"],
            "bpm_min": 128,
            "bpm_max": 140,
            "instruments": ["Synthetic bass", "Lead synth", "Kick", "Hi-hats", "Plucks"],
            "chords": [
                {"roman": "I – vi – iii – V", "C": "C – Am – Em – G"}
            ],
            "description": "Commercial EDM with big drops"
        },
        "Indie Pop": {
            "keywords": ["indie", "indie pop", "quirky", "cute", "fun", "独立流行"],
            "bpm_min": 100,
            "bpm_max": 130,
            "instruments": ["Clean guitar", "Bright synth", "Tambourine", "Bass", "Vocal harmonies"],
            "chords": [
                {"roman": "I – V – vi – IV", "C": "C – G – Am – F"}
            ],
            "description": "Quirky and fun indie pop"
        },
        "Ska": {
            "keywords": ["ska", "offbeat", "brass", "jamaica", "雷鬼"],
            "bpm_min": 130,
            "bpm_max": 160,
            "instruments": ["Off-beat guitar", "Brass section", "Walking bass", "Drums", "Organ"],
            "chords": [
                {"roman": "I – iv – V", "C": "C – F – G"}
            ],
            "description": "Upbeat ska with brass section"
        },
        "Punk Rock": {
            "keywords": ["punk", "aggressive", "fast", "distortion", "朋克"],
            "bpm_min": 150,
            "bpm_max": 200,
            "instruments": ["Distorted guitar", "Bass", "Drums", "Raw vocals", "Power chords"],
            "chords": [
                {"roman": "I – V", "C": "C – G"}
            ],
            "description": "Fast and aggressive punk rock"
        }
    }
    
    data = load_json("styles.json")
    for style, info in seed_styles.items():
        if style not in data:
            data[style] = info
    save_json("styles.json", data)
    print(f"✓ Added {len(seed_styles)} new styles")

def expand_emotions_from_seed_data():
    """Add more emotions from seed data"""
    seed_emotions = {
        "euphoric": {
            "keywords": ["euphoric", "ecstatic", "blissful", "elated", "狂喜", "极乐"],
            "description": "euphoric and ecstatic feeling"
        },
        "anxious": {
            "keywords": ["anxious", "tense", "nervous", "worried", "焦虑", "紧张"],
            "description": "anxious and tense atmosphere"
        },
        "confident": {
            "keywords": ["confident", "bold", "assertive", "powerful", "自信", "坚定"],
            "description": "confident and bold energy"
        },
        "lonely": {
            "keywords": ["lonely", "isolated", "solitary", "alone", "孤独", "寂寞"],
            "description": "lonely and isolated feeling"
        },
        "triumphant": {
            "keywords": ["triumphant", "victorious", "celebratory", "successful", "胜利", "凯旋"],
            "description": "triumphant and victorious atmosphere"
        }
    }
    
    data = load_json("emotions.json")
    for emotion, info in seed_emotions.items():
        if emotion not in data:
            data[emotion] = info
    save_json("emotions.json", data)
    print(f"✓ Added {len(seed_emotions)} new emotions")

def expand_references_from_predefined_lists():
    """Add reference tracks from curated lists"""
    seed_references = {
        "House": [
            ["Frankie Knuckles - The Whistle Song", "classic house anthem"],
            ["Daft Punk - One More Time", "filter house"],
            ["Armand Van Helden - You Don't Know Me", "vocal house"]
        ],
        "EDM": [
            ["Avicii - Wake Me Up", "folktronica EDM"],
            ["Swedish House Mafia - Don't You Worry Child", "progressive house"],
            ["Marshmello - Alone", "future bass"]
        ],
        "Indie Pop": [
            ["Phoenix - Lisztomania", "indie pop banger"],
            ["MGMT - Electric Feel", "indie electro pop"],
            ["Tame Impala - The Less I Know The Better", "indie psych pop"]
        ],
        "Ska": [
            ["The Specials - A Message to You, Rudy", "2-tone ska"],
            ["Reel Big Fish - Sell Out", "third wave ska"],
            ["No Doubt - Spiderwebs", "pop ska"]
        ],
        "Punk Rock": [
            ["The Ramones - Blitzkrieg Bop", "classic punk"],
            ["Green Day - Basket Case", "pop punk"],
            ["The Clash - London Calling", "punk rock epic"]
        ],
        "Jazz": [
            ["Miles Davis - So What", "modal jazz classic"],
            ["John Coltrane - Blue Train", "hard bop"],
            ["Bill Evans - Waltz for Debby", "jazz piano trio"],
            ["Kamasi Washington - The Truth", "modern jazz"],
            ["Robert Glasper - Black Radio", "jazz fusion"]
        ],
        "Folk": [
            ["Simon & Garfunkel - The Sound of Silence", "classic folk harmony"],
            ["Bon Iver - For Emma", "indie folk with falsetto"],
            ["Iron & Wine - Naked as We Came", "intimate folk"],
            ["Nick Drake - River Man", "melancholic folk"],
            ["Fleet Foxes - Mykonos", "harmony-rich folk"]
        ],
        "Metal": [
            ["Black Sabbath - Paranoid", "classic metal"],
            ["Metallica - Enter Sandman", "thrash metal anthem"],
            ["Dream Theater - Pull Me Under", "progressive metal"],
            ["Opeth - Ghost of Perdition", "progressive death metal"],
            ["Mastodon - Blood and Thunder", "sludge metal"]
        ]
    }
    
    data = load_json("references.json")
    for style, refs in seed_references.items():
        if style not in data:
            data[style] = refs
        else:
            # Add new references if not already present
            existing_titles = {r[0] for r in data[style]}
            for ref in refs:
                if ref[0] not in existing_titles:
                    data[style].append(ref)
    save_json("references.json", data)
    print(f"✓ Expanded references for {len(seed_references)} styles")

def expand_emotion_to_styles_mappings():
    """Add emotion-to-style mappings for new emotions and styles"""
    data = load_json("emotion_to_styles.json")
    
    # Add mappings for new emotions
    new_mappings = {
        "euphoric": {"EDM": 0.5, "House": 0.3, "Synthwave": 0.2},
        "anxious": {"Trip-hop": 0.4, "Post-rock": 0.3, "Ambient": 0.2, "Metal": 0.1},
        "confident": {"R&B": 0.3, "Synthwave": 0.3, "EDM": 0.2, "Metal": 0.2},
        "lonely": {"Ambient": 0.4, "Dream pop": 0.3, "Trip-hop": 0.2, "Folk": 0.1},
        "triumphant": {"Post-rock": 0.4, "Metal": 0.3, "EDM": 0.2, "Synthwave": 0.1},
        "playful": {"Indie Pop": 0.4, "Ska": 0.3, "Jazz": 0.2, "Lo-fi hiphop": 0.1},
        "dramatic": {"Post-rock": 0.4, "Metal": 0.3, "Trip-hop": 0.2, "Classical": 0.1},
        "serene": {"Ambient": 0.5, "Dream pop": 0.3, "Folk": 0.2}
    }
    
    for emotion, styles in new_mappings.items():
        if emotion not in data:
            data[emotion] = styles
    
    save_json("emotion_to_styles.json", data)
    print("✓ Updated emotion-to-style mappings")

# ============================================================================
# Helper Functions
# ============================================================================

def load_json(filename: str) -> dict:
    """Load JSON file"""
    filepath = DATA_DIR / filename
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return {}

def save_json(filename: str, data: dict):
    """Save JSON file"""
    filepath = DATA_DIR / filename
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"✓ Saved {filename}")

def main():
    print("=== SonicPalette Data Importer ===\n")
    
    print("1. Expanding styles...")
    expand_styles_from_seed_data()
    time.sleep(0.5)
    
    print("\n2. Expanding emotions...")
    expand_emotions_from_seed_data()
    time.sleep(0.5)
    
    print("\n3. Expanding references...")
    expand_references_from_predefined_lists()
    time.sleep(0.5)
    
    print("\n4. Expanding emotion-to-style mappings...")
    expand_emotion_to_styles_mappings()
    
    print("\n=== Data Expansion Complete ===")
    print("\nSummary:")
    print("- Styles added from seed data")
    print("- Emotions added from seed data")
    print("- Reference tracks expanded")
    print("- Emotion-to-style mappings updated")
    print("\nRun 'python app.py' or 'python gradio_ui.py' to use the expanded data!")

if __name__ == "__main__":
    main()

