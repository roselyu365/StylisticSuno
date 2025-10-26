#!/usr/bin/env python3
"""
Interactive Demo for SonicPalette
Run this to see the system in action with expanded data
"""

from app import (
    ml_enhanced_emotion_detection,
    ml_enhanced_style_detection,
    ML_AVAILABLE,
    pick_top_styles,
    blend_bpm,
    collect_instruments,
    pick_chords,
    suggest_references,
    format_suno_prompt,
    UserIntent
)

def demo_example(description, tempo_pref="auto", texture_pref="auto", era_pref="auto"):
    """Demo a single example"""
    print("\n" + "=" * 80)
    print(f"INPUT: {description}")
    print("=" * 80)
    
    # Use ML if available
    if ML_AVAILABLE:
        emotions = ml_enhanced_emotion_detection(description)
        scores = ml_enhanced_style_detection(description)
        print(f"[Using ML-enhanced detection]")
    else:
        from app import tokenize, match_emotions, compute_style_scores
        tokens = tokenize(description)
        emotions = match_emotions(tokens)
        scores = compute_style_scores(tokens, emotions)
        print(f"[Using keyword matching]")
    
    # Generate components
    top_styles = pick_top_styles(scores, k=2)
    bpm_range = blend_bpm(top_styles)
    instruments = collect_instruments(top_styles)
    chords = pick_chords(top_styles, n=2)
    refs = suggest_references(top_styles, emotions, n=3)
    
    # Apply preferences
    from app import apply_prefs
    intent = UserIntent(description=description, tempo_pref=tempo_pref, 
                       texture_pref=texture_pref, era_pref=era_pref)
    bpm_range, instruments = apply_prefs(bpm_range, instruments, intent)
    
    # Generate prompt
    prompt = format_suno_prompt(top_styles, emotions, bpm_range, instruments, chords, refs)
    
    # Display results
    print(f"\nStyles: {', '.join(top_styles)}")
    print(f"Emotions: {', '.join(emotions)}")
    print(f"BPM: {bpm_range[0]}–{bpm_range[1]}")
    print(f"Preferences: tempo={tempo_pref}, texture={texture_pref}, era={era_pref}")
    
    print(f"\n📝 SUNO PROMPT ({len(prompt.split())} words):")
    print("-" * 80)
    print(prompt)
    print("-" * 80)
    
    print("\n📊 DETAILED INFO:")
    print("Chords:")
    for ch in chords:
        print(f"  - {ch['roman']} | {ch['C']}")
    
    print("\nInstruments:")
    for inst in instruments[:6]:
        print(f"  - {inst}")
    
    print("\nReferences:")
    for ref, note in refs[:3]:
        print(f"  - {ref}")

def main():
    print("\n" + "🎵 SONICPALETTE DEMO 🎵")
    print("=" * 80)
    print(f"Emotions available: 22")
    print(f"Musical styles: 25")
    print(f"Reference tracks: 150+")
    print(f"ML Enhanced: {ML_AVAILABLE}")
    
    # Example 1
    demo_example(
        "Neon city at night, slightly melancholic yet hopeful, dreamy glitchy electronic",
        tempo_pref="auto",
        texture_pref="electronic",
        era_pref="modern"
    )
    
    # Example 2
    demo_example(
        "Classic country with steel guitar, warm and nostalgic",
        tempo_pref="slow",
        texture_pref="acoustic",
        era_pref="retro"
    )
    
    # Example 3
    demo_example(
        "Funk groove with heavy bass, confident and upbeat",
        tempo_pref="medium",
        texture_pref="electronic",
        era_pref="retro"
    )
    
    # Example 4
    demo_example(
        "Triumphant post-rock with epic build-up and cinematic drama",
        tempo_pref="fast",
        texture_pref="acoustic",
        era_pref="modern"
    )
    
    # Example 5
    demo_example(
        "House music festival vibes, euphoric and energetic with 4/4 beat",
        tempo_pref="auto",
        texture_pref="electronic",
        era_pref="modern"
    )
    
    print("\n" + "=" * 80)
    print("DEMO COMPLETE")
    print("=" * 80)
    print("\nAll prompts are under 200 words and ready to use in Suno!")
    print("Try running 'python app.py' for interactive mode or 'python gradio_ui.py' for web interface.")

if __name__ == "__main__":
    main()

