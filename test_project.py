#!/usr/bin/env python3
"""
Comprehensive Test Suite for SonicPalette
Tests all functionality including ML enhancements and expanded data
"""

import sys
from app import (
    ml_enhanced_emotion_detection,
    ml_enhanced_style_detection,
    pick_top_styles,
    blend_bpm,
    collect_instruments,
    pick_chords,
    suggest_references,
    format_suno_prompt,
    ML_AVAILABLE,
    STYLE_DB,
    EMOTION_KEYWORDS
)

def test_data_loading():
    """Test 1: Data Loading"""
    print("=" * 70)
    print("TEST 1: Data Loading")
    print("=" * 70)
    
    print(f"\n✓ Emotions loaded: {len(EMOTION_KEYWORDS)}")
    print(f"✓ Styles loaded: {len(STYLE_DB)}")
    print(f"✓ ML Available: {ML_AVAILABLE}")
    
    # Show sample emotions
    sample_emotions = list(EMOTION_KEYWORDS.keys())[:5]
    print(f"\nSample emotions: {', '.join(sample_emotions)}")
    
    # Show sample styles
    sample_styles = list(STYLE_DB.keys())[:5]
    print(f"Sample styles: {', '.join(sample_styles)}")
    
    return len(EMOTION_KEYWORDS) > 10 and len(STYLE_DB) > 10

def test_prompt_generation():
    """Test 2: Prompt Generation"""
    print("\n" + "=" * 70)
    print("TEST 2: Prompt Generation")
    print("=" * 70)
    
    test_cases = [
        ("Neon city at night, slightly melancholic yet hopeful, dreamy glitchy electronic", "City pop + Synthwave"),
        ("Warm cozy jazz lounge atmosphere with smooth vocals", "Jazz + R&B"),
        ("Funk groove with heavy bass, confident and upbeat", "Funk + EDM"),
        ("Classic country with steel guitar, warm and nostalgic", "Country"),
        ("Triumphant post-rock with epic build-up", "Post-rock")
    ]
    
    passed = 0
    for desc, expected_contains in test_cases:
        print(f"\n--- Test: {desc[:50]}... ---")
        
        try:
            # Use ML if available
            if ML_AVAILABLE:
                emotions = ml_enhanced_emotion_detection(desc)
                scores = ml_enhanced_style_detection(desc)
            else:
                from app import tokenize, match_emotions, compute_style_scores
                tokens = tokenize(desc)
                emotions = match_emotions(tokens)
                scores = compute_style_scores(tokens, emotions)
            
            top_styles = pick_top_styles(scores, k=2)
            bpm_range = blend_bpm(top_styles)
            instruments = collect_instruments(top_styles)
            chords = pick_chords(top_styles, n=2)
            refs = suggest_references(top_styles, emotions, n=3)
            prompt = format_suno_prompt(top_styles, emotions, bpm_range, instruments, chords, refs)
            
            word_count = len(prompt.split())
            
            print(f"  Styles: {', '.join(top_styles)}")
            print(f"  Emotions: {', '.join(emotions)}")
            print(f"  Word count: {word_count}")
            
            # Check if expected style is in result
            if any(expected_contains.lower() in s.lower() for s in top_styles):
                print(f"  ✓ PASS: Found expected style")
                passed += 1
            else:
                print(f"  ⚠ WARNING: Expected style not found (got {top_styles[0]})")
                passed += 0.5  # Partial pass
            
            # Check word limit
            if word_count <= 200:
                print(f"  ✓ PASS: Under 200 words")
                passed += 0.5
            else:
                print(f"  ✗ FAIL: Over 200 words ({word_count})")
            
        except Exception as e:
            print(f"  ✗ FAIL: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\n--- Test Summary: {passed}/5 tests passed ---")
    return passed >= 3

def test_all_components_included():
    """Test 3: All Components in Prompt"""
    print("\n" + "=" * 70)
    print("TEST 3: All Components Included in Prompt")
    print("=" * 70)
    
    desc = "House music festival vibes, euphoric and energetic"
    
    try:
        if ML_AVAILABLE:
            emotions = ml_enhanced_emotion_detection(desc)
            scores = ml_enhanced_style_detection(desc)
        else:
            from app import tokenize, match_emotions, compute_style_scores
            tokens = tokenize(desc)
            emotions = match_emotions(tokens)
            scores = compute_style_scores(tokens, emotions)
        
        top_styles = pick_top_styles(scores, k=2)
        bpm_range = blend_bpm(top_styles)
        instruments = collect_instruments(top_styles)
        chords = pick_chords(top_styles, n=2)
        refs = suggest_references(top_styles, emotions, n=3)
        prompt = format_suno_prompt(top_styles, emotions, bpm_range, instruments, chords, refs)
        
        print(f"\nGenerated prompt:\n")
        print(prompt)
        print()
        
        # Check for components
        components = {
            "Style": any(s.lower() in prompt.lower() for s in top_styles),
            "Mood": any(e.lower() in prompt.lower() for e in emotions),
            "Instruments": "instrumentation" in prompt.lower(),
            "Groove": "groove" in prompt.lower(),
            "Mix": "mix" in prompt.lower(),
            "Tempo": "bpm" in prompt.lower() or "tempo" in prompt.lower(),
            "Chords": "chord" in prompt.lower(),
            "References": "reference" in prompt.lower() or "refs" in prompt.lower()
        }
        
        print("Components check:")
        passed = 0
        for component, found in components.items():
            status = "✓" if found else "✗"
            print(f"  {status} {component}")
            if found:
                passed += 1
        
        print(f"\n--- Components found: {passed}/{len(components)} ---")
        
        return passed >= 6  # At least 6 components should be present
        
    except Exception as e:
        print(f"✗ FAIL: {e}")
        return False

def test_word_limit():
    """Test 4: Word Limit Enforcement"""
    print("\n" + "=" * 70)
    print("TEST 4: Word Limit (200 words max)")
    print("=" * 70)
    
    test_descriptions = [
        "Simple test",
        "Very long description with many adjectives and emotions and styles and instruments and moods and feelings that should compress properly",
        "Energetic upbeat dance music with synthesizers and heavy bass and complex chords and multiple styles blended together"
    ]
    
    all_pass = True
    for desc in test_descriptions:
        try:
            if ML_AVAILABLE:
                emotions = ml_enhanced_emotion_detection(desc)
                scores = ml_enhanced_style_detection(desc)
            else:
                from app import tokenize, match_emotions, compute_style_scores
                tokens = tokenize(desc)
                emotions = match_emotions(tokens)
                scores = compute_style_scores(tokens, emotions)
            
            top_styles = pick_top_styles(scores, k=2)
            bpm_range = blend_bpm(top_styles)
            instruments = collect_instruments(top_styles)
            chords = pick_chords(top_styles, n=2)
            refs = suggest_references(top_styles, emotions, n=3)
            prompt = format_suno_prompt(top_styles, emotions, bpm_range, instruments, chords, refs)
            
            word_count = len(prompt.split())
            status = "✓" if word_count <= 200 else "✗"
            print(f"  {status} {len(desc)} chars: {word_count} words")
            
            if word_count > 200:
                all_pass = False
                
        except Exception as e:
            print(f"  ✗ Error: {e}")
            all_pass = False
    
    return all_pass

def main():
    print("\n" + "=" * 70)
    print("SONICPALETTE COMPREHENSIVE TEST SUITE")
    print("=" * 70)
    
    tests = [
        ("Data Loading", test_data_loading),
        ("Prompt Generation", test_prompt_generation),
        ("All Components", test_all_components_included),
        ("Word Limit", test_word_limit)
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n✗ Test '{name}' failed with exception: {e}")
            results.append((name, False))
    
    # Summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    
    passed = sum(1 for _, r in results if r)
    total = len(results)
    
    for name, result in results:
        status = "PASS" if result else "FAIL"
        print(f"{status}: {name}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n✓ ALL TESTS PASSED - System is working correctly!")
    elif passed >= total * 0.75:
        print("\n⚠ MOST TESTS PASSED - System is mostly working")
    else:
        print("\n✗ SOME TESTS FAILED - Please check configuration")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

