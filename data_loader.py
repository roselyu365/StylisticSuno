#!/usr/bin/env python3
"""
Data loader for SonicPalette
Loads emotion keywords, styles, references, and emotion-to-style mappings from JSON files
Falls back to hardcoded data if files are not available
"""

import json
import os
from typing import Dict, List, Tuple
from pathlib import Path

# Get the directory where this file is located
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"

# ============================================================================
# Hardcoded fallback data (original data from app.py)
# ============================================================================

_FALLBACK_EMOTION_KEYWORDS = {
    "warm": ["warm", "cozy", "gentle", "soft", "tender", "温暖", "温柔"],
    "chill": ["chill", "laid-back", "relaxed", "轻松", "慵懒", "lofi"],
    "melancholic": ["melancholy", "melancholic", "sad", "blue", "emo", "忧郁", "伤感"],
    "energetic": ["energetic", "upbeat", "driving", "punchy", "热血", "劲", "动感"],
    "dreamy": ["dreamy", "hazy", "shimmer", "airy", "朦胧", "梦幻"],
    "dark": ["dark", "moody", "noir", "阴郁", "冷峻"],
    "romantic": ["romantic", "intimate", "甜", "浪漫"],
    "nostalgic": ["nostalgic", "retro", "vintage", "怀旧", "复古"],
    "urban": ["urban", "city", "neon", "霓虹", "夜色", "城市"],
    "tropical": ["tropical", "island", "reggae", "阳光", "海风"]
}

_FALLBACK_STYLE_DB = {
    "R&B": {
        "keywords": ["r&b", "soul", "neo-soul", "smooth", "silky", "urban", "late night", "柔滑"],
        "bpm": (70, 95),
        "instruments": ["Rhodes", "Electric piano", "Warm bass", "Soft kick & snare", "Silky synth pad", "Vocal layers"],
        "chords": [
            {"roman": "Imaj7 – vi7 – ii7 – V7", "C": "Cmaj7 – Am7 – Dm7 – G7"},
            {"roman": "ivmaj7 – V7 – iii7 – vi7", "C": "Fmaj7 – G7 – Em7 – Am7"},
            {"roman": "Imaj7 – iii7 – vi7 – ii7", "C": "Cmaj7 – Em7 – Am7 – Dm7"},
        ],
    },
    "Reggae": {
        "keywords": ["reggae", "dub", "tropical", "island", "sunny", "offbeat", "反拍", "牙买加"],
        "bpm": (60, 76),
        "instruments": ["Skank guitar (off-beat)", "Deep bass", "Dry drums", "Organ/Clav", "Spring reverb"],
        "chords": [
            {"roman": "I – V – vi – IV", "C": "C – G – Am – F"},
            {"roman": "ii – V – I", "C": "Dm – G – C"},
        ],
    },
    "Dream pop": {
        "keywords": ["dream pop", "shoegaze", "dreamy", "reverb", "浮游", "air", "hazy", "朦胧"],
        "bpm": (70, 95),
        "instruments": ["Shimmer guitar (reverb/delay)", "Airy pad", "Soft drums", "Chorus vocals", "Subtle synth"],
        "chords": [
            {"roman": "I – IV – Vsus – V", "C": "C – F – Gsus – G"},
            {"roman": "I – V – vi – IV", "C": "C – G – Am – F"},
        ],
    },
    "City pop": {
        "keywords": ["city pop", "retro", "80s", "japanese", "都会", "neon", "夜", "funky"],
        "bpm": (95, 115),
        "instruments": ["Electric guitar (clean)", "Slap/round bass", "Bright keys", "Disco hats", "Synth brass"],
        "chords": [
            {"roman": "Imaj7 – VI7 – ii7 – V7", "C": "Cmaj7 – A7 – Dm7 – G7"},
            {"roman": "Imaj7 – V/vi – vi – ii7 – V7", "C": "Cmaj7 – E7 – Am – Dm7 – G7"},
        ],
    },
    "Trip-hop": {
        "keywords": ["trip-hop", "moody", "noir", "downtempo", "vinyl", "阴郁", "港口雨夜"],
        "bpm": (70, 85),
        "instruments": ["Dusty drums", "Sub-bass", "Tape saturation", "Lo-fi keys", "Sparse samples"],
        "chords": [
            {"roman": "i – VI – III – VII (aeolian)", "C": "Am – F – C – G"},
            {"roman": "i – iv – v – i (minor)", "C": "Am – Dm – Em – Am"},
        ],
    },
    "Lo-fi hiphop": {
        "keywords": ["lofi", "study", "chill", "jazzy", "雨夜", "轻松"],
        "bpm": (65, 85),
        "instruments": ["Dusty drums", "Warm bass", "Rhodes", "Vinyl crackle", "Soft sax/keys"],
        "chords": [
            {"roman": "Imaj7 – vi7 – ii7 – V7", "C": "Cmaj7 – Am7 – Dm7 – G7"},
            {"roman": "ii7 – V7 – Imaj7", "C": "Dm7 – G7 – Cmaj7"},
        ],
    },
    "Synthwave": {
        "keywords": ["synthwave", "80s", "retro", "analog", "neon", "夜跑"],
        "bpm": (90, 110),
        "instruments": ["Analog polysynth", "Arp synth", "Gated reverb drums", "Punchy bass", "Chorus guitar"],
        "chords": [
            {"roman": "i – VI – III – VII (aeolian)", "C": "Am – F – C – G"},
            {"roman": "I – V – vi – IV", "C": "C – G – Am – F"},
        ],
    },
    "Post-rock": {
        "keywords": ["post-rock", "cinematic", "build-up", "延迟吉他", "层次", "情绪波峰"],
        "bpm": (80, 120),
        "instruments": ["Delay electric guitar", "Bass", "Drums (crescendo)", "Ambient pad", "Strings (optional)"],
        "chords": [
            {"roman": "I – IV – I – V (gradual build)", "C": "C – F – C – G"},
            {"roman": "vi – IV – I – V", "C": "Am – F – C – G"},
        ],
    },
    "Ambient": {
        "keywords": ["ambient", "drone", "space", "slow", "冥想", "空灵"],
        "bpm": (50, 80),
        "instruments": ["Evolving pads", "Texture drones", "Piano sparsely", "Field recordings", "Granular beds"],
        "chords": [
            {"roman": "I – IV – I (sustain)", "C": "C – F – C"},
            {"roman": "I – ii – I (modal)", "C": "C – Dm – C"},
        ],
    },
}

_FALLBACK_REFERENCE_DB = {
    "R&B": [
        ("The Weeknd - Earned It", "silky, urban R&B ballad"),
        ("FKJ - Tadow", "neo-soul, Rhodes & smooth bass"),
        ("Daniel Caesar - Best Part", "intimate R&B duet"),
    ],
    "Reggae": [
        ("Bob Marley - No Woman, No Cry", "classic roots reggae"),
        ("Toots & The Maytals - 54-46", "ska/rocksteady edge"),
        ("Rhye - Taste (reggae remix vibe)", "modern mellow twist"),
    ],
    "Dream pop": [
        ("Beach House - Space Song", "iconic hazy dream pop"),
        ("Alvvays - Dreams Tonite", "bright, nostalgic tint"),
        ("M83 - Midnight City", "synth-lush dreaminess"),
    ],
    "City pop": [
        ("Tatsuro Yamashita - Sparkle", "city pop gold"),
        ("Miki Matsubara - Stay With Me", "classic vibe"),
        ("落日飞车 Sunset Rollercoaster - My Jinji", "modern city-pop adjacent"),
    ],
    "Trip-hop": [
        ("Massive Attack - Teardrop", "moody, iconic trip-hop"),
        ("Portishead - Roads", "noir, cinematic"),
        ("Tricky - Hell Is Round The Corner", "dark texture"),
    ],
    "Lo-fi hiphop": [
        ("J Dilla - Donuts (various)", "lo-fi crate-digging vibe"),
        ("Nujabes - Feather", "jazzy chill"),
        ("Jinsang - affection", "classic lofi study"),
    ],
    "Synthwave": [
        ("Kavinsky - Nightcall", "retro analog mood"),
        ("Timecop1983 - On the Run", "romantic synthwave"),
        ("The Midnight - Sunset", "modern synthwave"),
    ],
    "Post-rock": [
        ("Explosions in the Sky - Your Hand in Mine", "build & catharsis"),
        ("Mono - Ashes in the Snow", "cinematic swell"),
        ("Wang Wen 惘闻 - Red Wall and Black Wall", "Chinese post-rock"),
    ],
    "Ambient": [
        ("Brian Eno - An Ending (Ascent)", "pioneering ambient"),
        ("Stars of the Lid - Requiem for Dying Mothers", "drone beauty"),
        ("Hammock - Turn Away and Return", "lush ambient"),
    ],
    "Indie refs": [
        ("黑裙子 - lingling", "Chinese indie electronic/alt reference"),
    ]
}

_FALLBACK_EMOTION_TO_STYLES = {
    "warm": {"R&B": 0.4, "Lo-fi hiphop": 0.3, "City pop": 0.2},
    "chill": {"Lo-fi hiphop": 0.4, "Dream pop": 0.3, "Ambient": 0.2},
    "melancholic": {"Trip-hop": 0.4, "Dream pop": 0.3, "Post-rock": 0.2},
    "energetic": {"City pop": 0.3, "Synthwave": 0.3, "Post-rock": 0.2},
    "dreamy": {"Dream pop": 0.5, "Ambient": 0.3, "Post-rock": 0.1},
    "dark": {"Trip-hop": 0.5, "Synthwave": 0.2, "Ambient": 0.2},
    "romantic": {"R&B": 0.4, "City pop": 0.3, "Dream pop": 0.2},
    "nostalgic": {"City pop": 0.4, "Synthwave": 0.3, "Lo-fi hiphop": 0.2},
    "urban": {"R&B": 0.4, "Trip-hop": 0.3, "Lo-fi hiphop": 0.2},
    "tropical": {"Reggae": 0.6, "City pop": 0.2},
}

# ============================================================================
# Loading functions
# ============================================================================

def load_json_file(filename: str) -> dict:
    """Load and parse a JSON file from the data directory"""
    filepath = DATA_DIR / filename
    if not filepath.exists():
        return None
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Warning: Could not load {filename}: {e}")
        return None

def load_emotion_keywords() -> Dict[str, List[str]]:
    """Load emotion keywords from JSON or fallback to hardcoded data"""
    data = load_json_file("emotions.json")
    if data is None:
        return _FALLBACK_EMOTION_KEYWORDS
    
    # Convert JSON format to expected format
    result = {}
    for emotion, info in data.items():
        result[emotion] = info.get("keywords", [])
    return result

def load_style_db() -> Dict:
    """Load style database from JSON or fallback to hardcoded data"""
    data = load_json_file("styles.json")
    if data is None:
        return _FALLBACK_STYLE_DB
    
    # Convert JSON format to expected format (convert bpm_min/max to tuple)
    result = {}
    for style, info in data.items():
        style_data = info.copy()
        if "bpm_min" in style_data and "bpm_max" in style_data:
            style_data["bpm"] = (style_data["bpm_min"], style_data["bpm_max"])
            del style_data["bpm_min"]
            del style_data["bpm_max"]
        result[style] = style_data
    return result

def load_reference_db() -> Dict[str, List[Tuple[str, str]]]:
    """Load reference database from JSON or fallback to hardcoded data"""
    data = load_json_file("references.json")
    if data is None:
        return _FALLBACK_REFERENCE_DB
    
    # Convert JSON format to expected format
    result = {}
    for style, refs in data.items():
        result[style] = [tuple(ref) for ref in refs]
    return result

def load_emotion_to_styles() -> Dict[str, Dict[str, float]]:
    """Load emotion-to-style mappings from JSON or fallback to hardcoded data"""
    data = load_json_file("emotion_to_styles.json")
    if data is None:
        return _FALLBACK_EMOTION_TO_STYLES
    return data

# ============================================================================
# Initialize global data
# ============================================================================

EMOTION_KEYWORDS = load_emotion_keywords()
STYLE_DB = load_style_db()
REFERENCE_DB = load_reference_db()
EMOTION_TO_STYLES = load_emotion_to_styles()

if __name__ == "__main__":
    # Test loading
    print("Loading data from JSON files...")
    print(f"Emotions loaded: {len(EMOTION_KEYWORDS)}")
    print(f"Styles loaded: {len(STYLE_DB)}")
    print(f"References loaded for {len(REFERENCE_DB)} styles")
    print(f"Emotion-to-style mappings: {len(EMOTION_TO_STYLES)}")
    
    print("\nExample emotions:", list(EMOTION_KEYWORDS.keys())[:5])
    print("Example styles:", list(STYLE_DB.keys())[:5])

