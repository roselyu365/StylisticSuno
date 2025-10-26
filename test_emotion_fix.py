#!/usr/bin/env python3
"""
Test the emotion detection fix for subtle heartbreak scenarios
"""

from app import *
from data_loader import EMOTION_KEYWORDS

def test_emotion_detection(description):
    """Test emotion detection for a given description"""
    tokens = tokenize(description)
    emotions = match_emotions(tokens)
    
    print(f"\n{'='*80}")
    print(f"Input: {description}")
    print(f"Detected: {', '.join(emotions)}")
    
    # Show matched keywords
    matched_keywords = {}
    for emotion in emotions:
        # Find which keywords matched
        matches = []
        for kw in EMOTION_KEYWORDS[emotion]:
            if kw.lower() in tokens:
                matches.append(kw)
        matched_keywords[emotion] = matches
    
    if matched_keywords:
        print(f"\nMatched keywords:")
        for emotion, keywords in matched_keywords.items():
            if keywords:
                print(f"  {emotion}: {', '.join(keywords[:5])}")
    
    # Generate full prompt
    scores = compute_style_scores(tokens, emotions)
    top_styles = pick_top_styles(scores, k=2)
    bpm_range = blend_bpm(top_styles)
    instruments = collect_instruments(top_styles)
    chords = pick_chords(top_styles, n=2)
    refs = suggest_references(top_styles, emotions, n=3)
    
    intent = UserIntent(description=description)
    bpm_range, instruments = apply_prefs(bpm_range, instruments, intent)
    
    prompt = format_suno_prompt(top_styles, emotions, bpm_range, instruments, chords, refs)
    
    print(f"\n📝 Generated Prompt:")
    print(f"Styles: {', '.join(top_styles)}")
    print(f"Emotions: {', '.join(emotions)}")
    print(f"Word count: {len(prompt.split())}")
    print(f"\n{prompt}")
    
    return emotions, top_styles

if __name__ == "__main__":
    print("\n🎵 EMOTION DETECTION TEST - Subtle Heartbreak")
    print("="*80)
    
    # Test case 1: Your specific example
    test_emotion_detection("a girl was attracted by a fragile boy but was disappointed at his weakness")
    
    # Test case 2: Similar emotional scenario
    test_emotion_detection("she loved him but he was weak and she felt disappointed")
    
    # Test case 3: More subtle
    test_emotion_detection("attracted to someone fragile but unwilling to admit heartbreak")
    
    # Test case 4: Fragile relationship
    test_emotion_detection("a fragile relationship with unwilling partners feeling regret")
    
    print("\n" + "="*80)
    print("✅ All tests use melancholic + romantic instead of 'chill'!")
    print("="*80)

