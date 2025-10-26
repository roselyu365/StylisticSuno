# 🎵 SonicPalette - Suno Prompt Builder

> **Enable users without music theory knowledge to generate Suno-ready music prompts in a single sentence**

SonicPalette is an intelligent prompt generator that transforms natural language descriptions into comprehensive, music-theory-informed prompts for Suno AI music generation. Simply describe the vibe you want, and get a complete composition blueprint with style, instruments, tempo, mood, chord progressions, and reference tracks.

view the songs I made with SonicPalette: https://suno.com/@roselyu9  ---super satisfied with the "Porcelain Heart"

## ✨ Features

### 🎯 Target Users
- **Creators unfamiliar with music theory** who want to create professional-sounding music
- **Beginners** learning about music production
- **Anyone** who wants to quickly generate "composition-ready" Suno prompts

### 🎨 What You Get

Every generated prompt includes:
- ✅ **Composition style** (e.g., Dream pop + R&B)
- ✅ **Tempo/speed** (BPM range, e.g., 70-95 BPM)
- ✅ **Mood/atmosphere** (e.g., melancholic, romantic, euphoric)
- ✅ **Instrument arrangement** (detailed instrumentation list)
- ✅ **Optional chord progressions** (Roman numerals + key examples)
- ✅ **Optional reference tracks** (song titles for style reference)
- ✅ **Structure suggestions** (intro, verse, chorus, bridge, outro)
- ✅ **Production tags** (groove, mix characteristics, effects)

### 🚀 Simple Workflow

```
Input natural-language description 
    ↓
One-click generate 
    ↓
Paste into Suno + Add lyrics
```

## 📦 Installation

### Requirements
- Python 3.8+
- pip

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/SonicPalette.git
cd SonicPalette

# Install dependencies
pip install -r requirements.txt
```

### Optional: ML Enhancement

For even better emotion and style detection:

```bash
pip install sentence-transformers
```

The system works perfectly without it, but ML mode provides more nuanced understanding of your descriptions.

## 🎮 Usage

### Option 1: Web Interface (Recommended)

```bash
python gradio_ui.py
```

Opens a beautiful web interface at `http://127.0.0.1:7860`

**Features:**
- Natural language input box
- Tempo, texture, and era preferences
- Instant prompt generation
- All components displayed clearly

### Option 2: Command Line

```bash
python app.py
```

Interactive CLI that guides you through:
1. Describe your vibe
2. Set preferences (tempo/texture/era)
3. Get complete prompt

### Option 3: Demo Script

```bash
python demo.py
```

See 5 example prompts with detailed output.

## 📝 Examples

### Example 1: City Pop Feel

**Input:**
```
Neon city at night, slightly melancholic yet hopeful, dreamy glitchy electronic
```

**Output:**
```
Dream pop + City pop style; melancholic, dreamy, urban mood; 
instrumentation: Shimmer guitar (reverb/delay), Airy pad, Soft drums, 
Chorus vocals, Subtle synth, Electric guitar (clean), Slap/round bass, 
Bright keys; groove: subtle swing, tasteful syncopation; mix: warm, 
silky, tape saturation, room reverb, sidechain, wide stereo; 
tempo: 82–105 BPM; chords: Imaj7 – VI7 – ii7 – V7 (Cmaj7 – A7 – Dm7 – G7); 
references: Stay With Me, Cat's Eye, Sugar for the Pill...
```

### Example 2: Subtle Heartbreak

**Input:**
```
a girl was attracted by a fragile boy but was disappointed at his weakness
```

**Output:**
```
Dream pop + R&B style; melancholic, romantic mood; 
instrumentation: Shimmer guitar (reverb/delay), Airy pad, Soft drums, 
Chorus vocals, Rhodes, Electric piano; groove: subtle swing; 
mix: warm, silky; tempo: 70–95 BPM; 
chords: I–vi7–ii7–V7; references: Earned It, Best Part...
```

### Example 3: Festival Vibes

**Input:**
```
House music festival vibes, euphoric and energetic with 4/4 beat
```

**Output:**
```
EDM + House style; energetic, euphoric mood; 
instrumentation: Synthetic bass, Lead synth, Four-on-floor kick, 
Piano chords, Hi-hats, Plucks; groove: subtle swing; 
mix: warm, silky; tempo: 124–135 BPM; 
chords: I–vi–iii–V; references: The Whistle Song, Alone...
```

## 🎵 Musical Styles Supported

### Core Styles
- **R&B** - Smooth, silky R&B with soulful vocals
- **Reggae** - Classic reggae with island vibes
- **Dream pop** - Hazy and dreamy with lush reverb
- **City pop** - Retro 80s Japanese city pop
- **Trip-hop** - Moody trip-hop with noir atmosphere
- **Lo-fi hip-hop** - Chill beats for study/relaxation
- **Synthwave** - Retro 80s synthwave with neon vibes
- **Post-rock** - Cinematic with epic build-ups
- **Ambient** - Atmospheric ambient textures

### Additional Styles
- **Jazz** - Classic jazz with swing feel
- **Folk** - Intimate folk with acoustic instruments
- **Metal** - Heavy metal with aggressive riffs
- **House** - Classic house with disco roots
- **EDM** - Commercial EDM with big drops
- **Indie Pop** - Quirky and fun indie pop
- **Ska** - Upbeat ska with brass section
- **Punk Rock** - Fast and aggressive punk
- **Country** - Classic country with steel guitar
- **Funk** - Groovy funk with syncopated rhythm
- **Blues** - Classic blues with soulful bends
- **Classical** - Orchestral classical music
- **Hip-Hop** - Classic hip-hop with 808 drums
- **Techno** - Driving techno with industrial edge
- **Gospel** - Uplifting gospel with choir
- **Soul** - Classic soul with horn section

## 😊 Emotions Detected

The system detects **22 different emotions**:
- warm, chill, melancholic, energetic, dreamy
- dark, romantic, nostalgic, urban, tropical
- playful, dramatic, serene, euphoric, anxious
- confident, lonely, triumphant, mysterious, contemplative
- festive, haunting

Each emotion maps to appropriate musical styles automatically.

## 🎹 What Makes This Special

### 1. No Music Theory Required
Describe your vibe in plain English. No need to know about:
- Chord progressions (system suggests them)
- BPM ranges (system calculates them)
- Instrumentation (system recommends it)

### 2. Intelligent Understanding
- ML-enhanced emotion detection
- Semantic style matching
- Keyword + context analysis
- Bilingual support (English + Chinese)

### 3. Production-Ready Output
Every prompt is:
- ✅ Under 200 words (Suno's limit)
- ✅ Includes all essential components
- ✅ Optimized for Suno AI
- ✅ Ready to paste and use

### 4. Rich Knowledge Base
- **25 musical styles** with detailed specifications
- **22 emotions** for nuanced mood capture
- **150+ reference tracks** for style guidance
- **Intelligent mixing** of styles based on your description

## 📁 Project Structure

```
SonicPalette/
├── app.py                    # Main application logic
├── gradio_ui.py              # Web interface
├── data_loader.py            # Data loading module
├── data/
│   ├── emotions.json         # 22 emotions with keywords
│   ├── styles.json           # 25 musical styles
│   ├── references.json       # 150+ reference tracks
│   └── emotion_to_styles.json
├── requirements.txt          # Dependencies
├── demo.py                   # Example demonstrations
├── test_project.py           # Test suite
└── manage_data.py            # Data management tool
```

## 🔧 Advanced Usage

### Customize Data

Add your own styles, emotions, or references:

```bash
# Edit data files directly
nano data/styles.json
nano data/emotions.json
nano data/references.json

# Or use management tool
python manage_data.py add-style
```

### Expand Knowledge Base

```bash
# Run data expansion scripts
python data_importer.py
python expand_data.py
```

This adds more styles, emotions, and references.

### Test the System

```bash
# Run comprehensive tests
python test_project.py

# Run emotion detection test
python test_emotion_fix.py
```

## 🎯 How It Works

### 1. Natural Language Processing
Your description is analyzed for:
- Keywords (emotions, styles, instruments, moods)
- Semantic meaning (ML-enhanced if available)
- Context and nuance

### 2. Style & Emotion Detection
- Matches detected emotions to musical styles
- Scores each style based on relevance
- Selects top 2 styles for blending

### 3. Prompt Assembly
- Blends BPM ranges
- Collects instruments from both styles
- Selects appropriate chord progressions
- Suggests reference tracks
- Applies user preferences

### 4. Smart Compression
- Ensures prompt stays under 200 words
- Prioritizes essential elements
- Adapts detail level automatically

### Output Components

Every prompt contains **8 components**:
1. **Style** - Musical genres (e.g., "Dream pop + City pop")
2. **Mood** - Detected emotions (e.g., "melancholic, romantic")
3. **Instruments** - Detailed arrangement (up to 8 instruments)
4. **Groove** - Rhythm characteristics (swing, syncopation)
5. **Mix** - Production style (warm, silky, etc.)
6. **Tempo** - BPM range (e.g., "70–95 BPM")
7. **Chords** - Optional progressions (Roman + key examples)
8. **References** - Optional song titles for style reference

## 🌟 Key Features

- **Zero music theory knowledge required**
- **One-sentence natural language input**
- **Comprehensive prompt generation** (style, mood, instruments, tempo, chords, references)
- **Smart compression** (always under 200 words)
- **22 emotions × 25 styles** = 550 possible combinations
- **Bilingual support** (English + Chinese)
- **ML-enhanced** (optional, for better understanding)
- **150+ reference tracks** for inspiration
- **Production-ready** output

## 📚 Documentation

- **[QUICK_START.md](QUICK_START.md)** - Get started quickly
- **[DATA_GUIDE.md](DATA_GUIDE.md)** - Customize data
- **[TEST_RESULTS.md](TEST_RESULTS.md)** - Test results
- **[CHANGES.md](CHANGES.md)** - Changelog
- **[GRADIO_USAGE.md](GRADIO_USAGE.md)** - Web interface guide

## 🎬 Getting Started

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Interface
```bash
python gradio_ui.py
```

### 3. Describe Your Song
```
a girl was attracted by a fragile boy but was disappointed at his weakness
```

### 4. Get Your Prompt
```
Dream pop + R&B style; melancholic, romantic mood; 
instrumentation: Shimmer guitar, Airy pad, Rhodes, Electric piano...
```

### 5. Use in Suno
- Copy the prompt
- Paste into Suno's prompt field
- Add your lyrics using the same description
- Generate!

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Add more musical styles
- Expand emotion detection
- Add reference tracks
- Improve ML model
- Add more languages

## 📄 License

See [LICENSE](LICENSE) file.

## 🙏 Acknowledgments

Built with love for creators who want to make music without barriers. 

Special thanks to:
- Suno AI for inspiration
- The music theory that made this possible
- All the artists in the reference database

## 💡 Pro Tips

1. **Be specific** - More details = better prompts
2. **Mix emotions** - "melancholic yet hopeful" works great
3. **Mention instruments** - "with steel guitar" helps
4. **Set preferences** - Tempo/texture/era fine-tune output
5. **Use references** - Mention songs for style guidance

## 📞 Support

- **Issues**: Open an issue on GitHub
- **Questions**: Check documentation files
- **Suggestions**: Submit a feature request

---

**Made for creators who want to make music, not struggle with music theory.**

Happy creating! 🎵✨
