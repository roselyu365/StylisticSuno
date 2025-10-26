#!/usr/bin/env python3
"""Quick test script to verify ML-enhanced prompt generation"""

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

def test_prompt_generation():
    print("=" * 60)
    print("Testing ML-Enhanced Suno Prompt Builder")
    print("=" * 60)
    
    # Test descriptions
    test_cases = [
        "Neon city at night, slightly melancholic yet hopeful, dreamy glitchy electronic",
        "Warm and cozy jazz lounge atmosphere with smooth vocals",
        "Rainy night chill vibes with lo-fi beats",
        "Energetic summer beach party music",
    ]
    
    for i, desc in enumerate(test_cases, 1):
        print(f"\n{'='*60}")
        print(f"Test Case {i}: {desc}")
        print(f"{'='*60}\n")
        
        try:
            # Use ML detection
            if ML_AVAILABLE:
                print("✅ Using ML-enhanced detection...")
                emotions = ml_enhanced_emotion_detection(desc)
                scores = ml_enhanced_style_detection(desc)
            else:
                print("⚠️  ML not available, using keyword matching...")
                from app import tokenize, match_emotions, compute_style_scores
                tokens = tokenize(desc)
                emotions = match_emotions(tokens)
                scores = compute_style_scores(tokens, emotions)
            
            # Generate components
            top_styles = pick_top_styles(scores, k=2)
            bpm_range = blend_bpm(top_styles)
            instruments = collect_instruments(top_styles)
            chords = pick_chords(top_styles, n=2)
            refs = suggest_references(top_styles, emotions, n=3)
            
            # Create intent (using defaults)
            intent = UserIntent(description=desc)
            
            # Generate prompt
            prompt = format_suno_prompt(top_styles, emotions, bpm_range, instruments, chords, refs)
            
            # Display results
            print(f"Styles: {', '.join(top_styles)}")
            print(f"Emotions: {', '.join(emotions)}")
            print(f"BPM: {bpm_range[0]}–{bpm_range[1]}")
            print(f"\n📝 Generated Prompt ({len(prompt.split())} words):\n")
            print(prompt)
            
            if len(prompt.split()) > 200:
                print(f"⚠️  Warning: Prompt exceeds 200 words ({len(prompt.split())} words)")
            else:
                print(f"✅ Prompt is under 200 words ({len(prompt.split())} words)")
                
        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "=" * 60)
    print("Test Complete")
    print("=" * 60)

if __name__ == "__main__":
    test_prompt_generation()

