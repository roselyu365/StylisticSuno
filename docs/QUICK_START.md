# Quick Start Guide

## Installation

```bash
pip install -r requirements.txt
```

## Basic Usage

### Web Interface (Recommended)

```bash
python gradio_ui.py
```

Then open the browser to the URL shown.

### Command Line

```bash
python app.py
```

Follow the prompts to generate your Suno prompt.

## Example Inputs

### Chill Vibes
```
Input: Rainy night chill vibes with lo-fi beats
Output: [Lo-fi hiphop + Dream pop style; chill, melancholic mood; ...]
```

### City Pop
```
Input: Neon city at night, 80s retro synthesizers, nostalgic
Output: [City pop + Synthwave style; urban, nostalgic mood; ...]
```

### Warm R&B
```
Input: Smooth silky R&B with warm vocals and Rhodes piano
Output: [R&B + Lo-fi hiphop style; warm, romantic mood; ...]
```

## What's in the Prompt?

Every generated prompt includes:
- ✅ **Style**: Musical styles (e.g., "R&B + Dream pop")
- ✅ **Mood**: Detected emotions (e.g., "warm, romantic")
- ✅ **Instruments**: Up to 8 instruments
- ✅ **Groove**: Swing and syncopation style
- ✅ **Mix**: Audio processing (warm/silky/moody/etc.)
- ✅ **Tempo**: BPM range (e.g., "75–90 BPM")
- ✅ **Chords**: Progressions with examples (NEW!)
- ✅ **References**: Similar artists/tracks (NEW!)
- ✅ **Structure**: Song arrangement (optional)

**All under 200 words!**

## ML vs Keyword Mode

### With ML (Installed)
- Better intent understanding
- Semantic similarity matching
- Hybrid approach (70% ML, 30% keywords)
- More accurate style detection

### Without ML (Fallback)
- Keyword matching only
- Still produces good results
- All features work

## Tips

1. Be descriptive about the feeling or atmosphere
2. Mention instruments if you have preferences
3. Use emotional keywords (warm, melancholic, energetic, etc.)
4. Mix English and Chinese if needed
5. Adjust tempo/texture/era preferences as needed

## Testing

Run the test script to see examples:

```bash
python test_ml_prompt.py
```

## Troubleshooting

**Import errors?**
```bash
pip install sentence-transformers numpy torch gradio
```

**Prompt too long?**
- The compression algorithm handles this automatically
- If it still exceeds 200 words, the structure section is typically removed first

**ML not working?**
- Check that `sentence-transformers` is installed
- System will use keyword matching as fallback
- You'll see a warning message

