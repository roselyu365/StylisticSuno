# Data Management Guide

## Overview

The SonicPalette prompt builder now uses external JSON files for data management, making it easy to add, modify, and expand the musical knowledge base.

## Directory Structure

```
data/
├── emotions.json              # Emotion keywords and descriptions
├── styles.json                # Musical style definitions
├── references.json           # Reference tracks for each style
└── emotion_to_styles.json    # Emotion-to-style weight mappings
```

## How to Expand Data

### 1. Adding New Emotions

Edit `data/emotions.json`:

```json
{
    "playful": {
        "keywords": ["playful", "fun", "bouncy", "whimsical", "有趣", "跳跃"],
        "description": "playful and fun mood"
    }
}
```

### 2. Adding New Musical Styles

Edit `data/styles.json`:

```json
{
    "Techno": {
        "keywords": ["techno", "4/4", "industrial", "berlin", "电子"],
        "bpm_min": 120,
        "bpm_max": 150,
        "instruments": ["Kick drum", "Bass synth", "Hi-hats", "Stabs"],
        "chords": [
            {"roman": "i – i – i – i (minimal)", "C": "Am – Am – Am – Am"}
        ],
        "description": "Driving techno with industrial edge"
    }
}
```

### 3. Adding Reference Tracks

Edit `data/references.json`:

```json
{
    "Techno": [
        ["Jeff Mills - The Bells", "classic techno anthem"],
        ["Underworld - Born Slippy", "big beat techno"],
        ["Charlotte de Witte - Selected", "hard techno"]
    ]
}
```

### 4. Adding Emotion-to-Style Mappings

Edit `data/emotion_to_styles.json`:

```json
{
    "playful": {
        "City pop": 0.4,
        "Jazz": 0.3,
        "Lo-fi hiphop": 0.2,
        "Techno": 0.1
    }
}
```

## Using the Management Tool

### List All Styles

```bash
python manage_data.py list-styles
```

### List All Emotions

```bash
python manage_data.py list-emotions
```

### Add a New Style (Interactive)

```bash
python manage_data.py add-style
```

This will prompt you for:
- Style name
- Keywords
- BPM range
- Instruments
- Chord progressions
- Description

### View a Data File

```bash
python manage_data.py view emotions.json
python manage_data.py view styles.json
```

## File Formats

### emotions.json

```json
{
    "emotion_name": {
        "keywords": ["keyword1", "keyword2", "中文关键词"],
        "description": "Description of the emotion"
    }
}
```

### styles.json

```json
{
    "Style Name": {
        "keywords": ["keyword1", "keyword2"],
        "bpm_min": 70,
        "bpm_max": 95,
        "instruments": ["Instrument 1", "Instrument 2"],
        "chords": [
            {"roman": "I – vi – IV – V", "C": "C – Am – F – G"}
        ],
        "description": "Style description"
    }
}
```

### references.json

```json
{
    "Style Name": [
        ["Artist - Song Title", "description/note"],
        ["Artist 2 - Song 2", "note"]
    ]
}
```

### emotion_to_styles.json

```json
{
    "emotion_name": {
        "Style Name": 0.4,
        "Another Style": 0.3,
        "Third Style": 0.2
    }
}
```

## Adding Your Own Data

### Quick Add Examples

#### Add a New Emotion
1. Open `data/emotions.json`
2. Add your emotion with keywords
3. Run the app - it will automatically use the new emotion

#### Add a New Style
1. Open `data/styles.json`
2. Add your style with all required fields
3. Optionally add references in `data/references.json`
4. Update `data/emotion_to_styles.json` to link emotions to your new style

#### Add Reference Tracks
1. Open `data/references.json`
2. Find the style you want to add to
3. Add `["Artist - Song", "description"]`
4. Save the file

## Best Practices

1. **Keywords**: Include both English and Chinese keywords for bilingual support
2. **Descriptions**: Keep descriptions concise but informative
3. **BPM Ranges**: Use realistic BPM ranges for the style
4. **Instruments**: List 4-6 characteristic instruments
5. **Chord Progressions**: Provide both Roman numeral and key-specific examples
6. **References**: Include diverse, representative tracks

## Testing Your Changes

After modifying data files:

```bash
# Test data loading
python data_loader.py

# Test the app
python app.py

# Test with ML
python test_ml_prompt.py
```

## Examples

### Example: Adding "Blues" Style

**In `data/styles.json`:**
```json
{
    "Blues": {
        "keywords": ["blues", "12-bar", "soulful", "bend", "布鲁斯"],
        "bpm_min": 60,
        "bpm_max": 110,
        "instruments": ["Electric guitar", "Harp", "Slide guitar", "Drums", "Bass"],
        "chords": [
            {"roman": "I – I – I – I – IV – IV – I – I – V – IV – I – I", "C": "C – C – C – C – F – F – C – C – G – F – C – C"}
        ],
        "description": "Classic blues with soulful guitar bends"
    }
}
```

**In `data/references.json`:**
```json
{
    "Blues": [
        ["B.B. King - The Thrill Is Gone", "classic blues ballad"],
        ["Stevie Ray Vaughan - Pride and Joy", "electric blues"],
        ["Muddy Waters - Mannish Boy", "blues standard"]
    ]
}
```

**In `data/emotion_to_styles.json`:**
```json
{
    "melancholic": {
        "Trip-hop": 0.4,
        "Dream pop": 0.3,
        "Post-rock": 0.2,
        "Blues": 0.1
    }
}
```

## Troubleshooting

### Data Not Loading?
- Check that `data/` directory exists
- Verify JSON syntax (no trailing commas)
- Run `python data_loader.py` to test

### Old Data Showing?
- Clear Python cache: `rm -rf __pycache__`
- Restart the app

### Import Error?
- Ensure `data_loader.py` is in the same directory as `app.py`
- Check for syntax errors in JSON files

