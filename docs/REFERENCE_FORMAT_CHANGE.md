# Reference Format Change ✅

## What Changed

The reference tracks in the final prompt now show **only song titles** instead of "Artist - Song Title" format.

## Before vs After

### Before:
```
references: The Weeknd, Beach House, Tatsuro Yamashita
```

or in the prompt:
```
references: The Weeknd - Earned It, Beach House - Space Song, Tatsuro Yamashita - Sparkle
```

### After:
```
references: Earned It, Space Song, Sparkle
```

Just the song titles!

## Example Output

### Input:
```
"Neon city at night, slightly melancholic yet hopeful, dreamy glitchy electronic"
```

### Prompt Output:
```
...tempo: 82–105 BPM; chords: I – IV – Vsus – V (C – F – Gsus – G); 
references: Stay With Me, Cat's Eye, Sugar for the Pill; structure: 
intro – verse – chorus – verse – bridge – outro.
```

**Note:** Song titles only! ✅

## Detailed Info Still Shows Artist

The detailed information section still shows the full format:
```
References:
  - Miki Matsubara - Stay With Me
  - Anri - Cat's Eye
  - Slowdive - Sugar for the Pill
```

This is helpful for users who want to know the full artist-track info.

## Benefits

1. **Cleaner prompts** - More concise
2. **Less word count** - Fits better under 200 words
3. **Focus on music** - Emphasizes the track characteristics
4. **Still informative** - Song titles are clear references

## Code Change

Changed in `app.py` around line 454-465:

**Old code:**
```python
ref_names.append(artist_name)  # Extracted artist name
```

**New code:**
```python
song_title = ref[0].split(' - ', 1)[1]  # Extract song title
ref_titles.append(song_title)
```

## Testing

All tests pass ✅
- Components included: 8/8
- Word limit: Under 200
- Compression: Working
- Format: Song titles only

## Verification

Run the demo to see the change:
```bash
python demo.py
```

You'll see prompts like:
- `references: Stay With Me, Cat's Eye, Sugar for the Pill`
- `references: Lisztomania, Jolene, The Less I Know The Better`
- `references: The Less I Know The Better, Wake Up, You Don't Know Me`

All song titles only! 🎵

