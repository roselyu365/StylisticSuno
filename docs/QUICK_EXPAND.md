# Quick Data Expansion Guide

## Expand Your Data in 3 Steps

### Step 1: Run the Importer

```bash
python data_importer.py
```

This adds:
- ✅ 5 new styles (House, EDM, Indie Pop, Ska, Punk Rock)
- ✅ 5 new emotions
- ✅ Reference tracks

### Step 2: Run the Full Expansion

```bash
python expand_data.py
```

This adds:
- ✅ 8 more styles (Country, Funk, Blues, Classical, Hip-Hop, Techno, Gospel, Soul)
- ✅ 5 more emotions
- ✅ More reference tracks

### Step 3: Verify

```bash
python data_loader.py
```

Expected output:
```
Emotions loaded: 22
Styles loaded: 25
References loaded for 26 styles
```

## Before & After

### Before Expansion
- Emotions: 13
- Styles: 12
- References: ~40 tracks

### After Expansion
- Emotions: **22** (+9)
- Styles: **25** (+13)
- References: **150+ tracks** (+110+)

## What You Get

### New Styles Added

**From data_importer.py:**
- House
- EDM
- Indie Pop
- Ska
- Punk Rock

**From expand_data.py:**
- Country
- Funk
- Blues
- Classical
- Hip-Hop
- Techno
- Gospel
- Soul

### New Emotions Added

- euphoric, anxious, confident, lonely, triumphant
- mysterious, contemplative, festive, haunting

## Test It Out

```bash
# Test the expanded data
python app.py

# Or use web interface
python gradio_ui.py
```

Try these examples:
- "House music festival vibes, euphoric"
- "Classic country with steel guitar"
- "Funk groove with heavy bass"
- "Haunting blues with slide guitar"

## Customize

Edit the data files directly:
```bash
nano data/styles.json      # Add more styles
nano data/emotions.json    # Add more emotions
nano data/references.json # Add more references
```

Or use the management tool:
```bash
python manage_data.py add-style
```

## Next Steps

1. **Add even more styles** - Edit JSON files
2. **Customize references** - Add your favorite tracks
3. **Tweak emotions** - Add nuance to emotion detection
4. **Integrate APIs** - See EXTERNAL_DATA_SOURCES.md

## Quick Commands

```bash
# List all styles
python manage_data.py list-styles

# View a file
python manage_data.py view styles.json

# Test data loading
python data_loader.py

# Run the app
python app.py
```

