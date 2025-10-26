# External Data Sources Guide

## Overview

The SonicPalette system now supports importing data from external sources to expand the knowledge base. This document explains how to use these features.

## Data Expansion Scripts

### 1. `data_importer.py` - Basic Seed Data

Imports curated seed data from predefined lists:

```bash
python data_importer.py
```

**What it adds:**
- 5 new styles: House, EDM, Indie Pop, Ska, Punk Rock
- 5 new emotions: euphoric, anxious, confident, lonely, triumphant
- Reference tracks for new styles
- Updated emotion-to-style mappings

**Before running:**
- Emotions: 13
- Styles: 12
- References: 13 styles

**After running:**
- Emotions: 18
- Styles: 17
- References: 21 styles

### 2. `expand_data.py` - Comprehensive Expansion

Imports genre-specific data from curated knowledge base:

```bash
python expand_data.py
```

**What it adds:**
- 8 new styles: Country, Funk, Blues, Classical, Hip-Hop, Techno, Gospel, Soul
- 5 new emotions: mysterious, triumphant, contemplative, festive, haunting
- Reference tracks for all new styles
- Comprehensive coverage

**Final counts after both scripts:**
- Emotions: 22
- Styles: 25
- References: 26 styles

## Data Sources Used

### 1. Wikipedia / Music Genre Lists

Our curated expansion uses widely recognized genres from:
- Popular music taxonomy
- Academic music classification
- Streaming platform categorization

### 2. Reference Track Sources

Reference tracks are curated from:
- Critical music canon
- Streaming platform "essential" playlists
- Music education resources
- Cultural touchstones

### 3. Instrumentation Data

Instrument lists drawn from:
- Genre-specific practices
- Music production norms
- Cultural context

## How to Add More External Sources

### Option 1: Last.fm API

Add Last.fm API key to fetch artist data:

1. Get API key: https://www.last.fm/api
2. Edit `data_importer.py`:

```python
def fetch_artist_top_tracks(artist_name: str) -> List[tuple]:
    # Add your Last.fm API key here
    api_key = "YOUR_API_KEY"
    # ... fetch data ...
```

### Option 2: Spotify API

Add Spotify integration for track discovery:

1. Get API credentials: https://developer.spotify.com/
2. Install Spotify SDK: `pip install spotipy`
3. Add to `data_importer.py`:

```python
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def fetch_spotify_genre_tracks(genre: str, api_key: str, api_secret: str):
    client_credentials = SpotifyClientCredentials(
        client_id=api_key,
        client_secret=api_secret
    )
    sp = spotipy.Spotify(client_credentials_manager=client_credentials)
    
    results = sp.search(q=f'genre:"{genre}"', type='track', limit=5)
    # Process results...
```

### Option 3: MusicBrainz API

Fetch album/release data:

```python
def fetch_musicbrainz_data(artist: str):
    url = "https://musicbrainz.org/ws/2/release-group"
    # Requires proper headers and formatting
```

### Option 4: Web Scraping

Scrape popular music sites (legal and ethical):

```python
import requests
from bs4 import BeautifulSoup

def scrape_genre_references(genre: str):
    url = f"https://rateyourmusic.com/genre/{genre}"
    # Parse HTML...
```

## Integration Examples

### Example: Fetching from Multiple APIs

Create `fetch_from_apis.py`:

```python
#!/usr/bin/env python3
import spotipy
from data_importer import DataExpander

class AdvancedDataExpander(DataExpander):
    def fetch_from_spotify(self, genre: str):
        # Spotify API implementation
        pass
    
    def fetch_from_lastfm(self, artist: str):
        # Last.fm API implementation
        pass
    
    def merge_all_sources(self):
        """Merge data from all sources"""
        # Fetch from Spotify
        spotify_data = self.fetch_from_spotify("techno")
        
        # Fetch from Last.fm
        lastfm_data = self.fetch_from_lastfm("Charlotte de Witte")
        
        # Merge and deduplicate
        merged = self.merge_reference_lists(spotify_data, lastfm_data)
        return merged
```

### Example: Using Public Datasets

```python
def import_from_dataset():
    """Import from public music datasets"""
    # Example: Million Song Dataset
    # Example: Discogs data
    # Example: MusicBrainz dump
    pass
```

## Data Quality Guidelines

When adding external data, ensure:

1. **Accuracy**: Verify genre classifications
2. **Relevance**: Include representative examples
3. **Diversity**: Include various subgenres
4. **Cultural Context**: Include non-Western music
5. **Balance**: Mix classic and contemporary
6. **Avoid Duplicates**: Check existing references
7. **Format Consistency**: Follow JSON schema
8. **Bilingual**: Include Chinese keywords

## Testing Imported Data

After importing data:

```bash
# Verify data loaded correctly
python data_loader.py

# Test with examples
python app.py

# Check for duplicates
python -c "from data_loader import STYLE_DB; print(len(STYLE_DB))"
```

## Scheduled Updates

Create an update script `update_external_data.py`:

```python
#!/usr/bin/env python3
"""Schedule regular data updates from external sources"""

import schedule
import time

def update_data():
    print("Updating data from external sources...")
    # Run data_importer.py
    # Run expand_data.py
    # Verify integrity
    print("Data update complete")

# Schedule daily updates
schedule.every().day.at("02:00").do(update_data)

while True:
    schedule.run_pending()
    time.sleep(3600)
```

## Security Considerations

When using external APIs:

1. **API Keys**: Never commit keys to repository
2. **Rate Limiting**: Respect API rate limits
3. **Error Handling**: Handle network failures
4. **Data Validation**: Verify imported data
5. **Privacy**: Don't store user data without consent

Use environment variables for API keys:

```python
import os

LASTFM_API_KEY = os.getenv('LASTFM_API_KEY')
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
```

## Current Data Statistics

After running both expansion scripts:

| Metric | Count | Coverage |
|--------|-------|----------|
| Emotions | 22 | Comprehensive |
| Styles | 25 | Major genres covered |
| Reference Tracks | 26 styles | 5-15 per style |
| Emotion-Style Mappings | 18 | Full coverage |

### Genres Included

**Popular Genres:**
- R&B, Reggae, Dream pop, City pop, Trip-hop, Lo-fi hip-hop, Synthwave, Post-rock, Ambient

**Additional Genres:**
- House, EDM, Indie Pop, Ska, Punk Rock (added by data_importer.py)
- Country, Funk, Blues, Classical, Hip-Hop, Techno, Gospel, Soul (added by expand_data.py)

**Musical Styles:**
- Jazz, Folk, Metal (already included)

## Future Enhancements

1. **API Integration**: Add Spotify/Last.fm API support
2. **Auto-Update**: Schedule automatic updates
3. **User Contributions**: Allow users to submit tracks
4. **ML-Based Discovery**: Use ML to find similar tracks
5. **Multilingual**: Add more languages beyond English/Chinese
6. **Subgenre Support**: Add subgenre classifications
7. **Mood Detection**: Use ML to detect track moods
8. **Temporal Tags**: Add decade/era tags

## Troubleshooting

**Import fails?**
- Check internet connection
- Verify JSON file syntax
- Ensure data directory exists

**API rate limits?**
- Add delays between requests
- Cache results
- Use batch requests

**Duplicate tracks?**
- Use deduplication logic
- Check existing references before adding

## Resources

- Music API Documentation: https://github.com/topics/music-api
- Music Datasets: https://github.com/crowdAI/music-challenges
- MusicBrainz: https://musicbrainz.org/doc/MusicBrainz_API
- Spotify API: https://developer.spotify.com/documentation/web-api/

