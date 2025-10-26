#!/usr/bin/env python3
"""
Enhanced Data Expansion Tool
Fetches data from multiple sources to expand the knowledge base
"""

import json
import requests
from pathlib import Path
from typing import Dict, List
import time

DATA_DIR = Path("data")

class DataExpander:
    def __init__(self):
        self.data_dir = DATA_DIR
        
    def load_json(self, filename: str) -> dict:
        """Load JSON file"""
        filepath = self.data_dir / filename
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def save_json(self, filename: str, data: dict):
        """Save JSON file"""
        filepath = self.data_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"✓ Saved {filename}")
    
    def add_musical_styles_from_wikipedia_genres(self):
        """Add popular music genres from a curated list"""
        genres_data = {
            "Country": {
                "keywords": ["country", "western", "twang", "guitar", "countryside", "乡村"],
                "bpm_min": 70,
                "bpm_max": 120,
                "instruments": ["Acoustic guitar", "Steel guitar", "Fiddle", "Banjo", "Harmonica"],
                "chords": [
                    {"roman": "I – V – I", "C": "C – G – C"},
                    {"roman": "I – IV – V – I", "C": "C – F – G – C"}
                ],
                "description": "Classic country music with twangy guitar"
            },
            "Funk": {
                "keywords": ["funk", "groove", "slap bass", "syncopated", "funky", "放克"],
                "bpm_min": 100,
                "bpm_max": 130,
                "instruments": ["Slap bass", "Wah guitar", "Horn section", "Organ", "Drum kit"],
                "chords": [
                    {"roman": "i7 – v7", "C": "C7 – G7"},
                    {"roman": "ii7 – V7 – I7", "C": "Dm7 – G7 – C7"}
                ],
                "description": "Groovy funk with syncopated rhythm"
            },
            "Blues": {
                "keywords": ["blues", "12-bar", "soulful", "bend", "布鲁斯"],
                "bpm_min": 60,
                "bpm_max": 110,
                "instruments": ["Electric guitar", "Harp", "Slide guitar", "Drums", "Bass"],
                "chords": [
                    {"roman": "I – I – I – I – IV – IV – I – I – V – IV – I – I", "C": "C – C – C – C – F – F – C – C – G – F – C – C"}
                ],
                "description": "Classic blues with soulful guitar bends"
            },
            "Classical": {
                "keywords": ["classical", "orchestral", "symphony", "piano", "strings", "古典"],
                "bpm_min": 40,
                "bpm_max": 140,
                "instruments": ["Piano", "Strings section", "Woodwinds", "Brass", "Timpani"],
                "chords": [
                    {"roman": "I – vi – IV – V", "C": "C – Am – F – G"},
                    {"roman": "I – V – vi – IV", "C": "C – G – Am – F"}
                ],
                "description": "Orchestral classical music"
            },
            "Hip-Hop": {
                "keywords": ["hip-hop", "rap", "808", "turntable", "sayings", "说唱"],
                "bpm_min": 70,
                "bpm_max": 100,
                "instruments": ["808 kick", "Snare", "Hi-hats", "Sub-bass", "Samples"],
                "chords": [
                    {"roman": "i – i – i – i", "C": "Am – Am – Am – Am"},
                    {"roman": "i – VI – v – VI", "C": "Am – F – Em – F"}
                ],
                "description": "Classic hip-hop with 808 drums"
            },
            "Techno": {
                "keywords": ["techno", "4/4", "industrial", "minimal", "machine", "科技"],
                "bpm_min": 120,
                "bpm_max": 150,
                "instruments": ["Kick drum", "Bass synth", "Hi-hats", "Stabs", "Atmospheric pads"],
                "chords": [
                    {"roman": "i – i – i – i", "C": "Am – Am – Am – Am"}
                ],
                "description": "Driving techno with industrial edge"
            },
            "Gospel": {
                "keywords": ["gospel", "choir", "spiritual", "uplifting", "faith", "福音"],
                "bpm_min": 80,
                "bpm_max": 120,
                "instruments": ["Choir", "Organ", "Piano", "Horns", "Tambourine"],
                "chords": [
                    {"roman": "I – IV – V", "C": "C – F – G"}
                ],
                "description": "Uplifting gospel with choir"
            },
            "Soul": {
                "keywords": ["soul", "motown", "smooth", "groove", "horn", "灵魂"],
                "bpm_min": 80,
                "bpm_max": 120,
                "instruments": ["Soul vocals", "Horns section", "Electric organ", "Bass", "Drums"],
                "chords": [
                    {"roman": "I – vi – IV – V", "C": "C – Am – F – G"}
                ],
                "description": "Classic soul with horn section"
            }
        }
        
        data = self.load_json("styles.json")
        added = 0
        for style, info in genres_data.items():
            if style not in data:
                data[style] = info
                added += 1
        
        if added > 0:
            self.save_json("styles.json", data)
            print(f"✓ Added {added} new styles")
        else:
            print("No new styles to add")
    
    def add_comprehensive_reference_tracks(self):
        """Add comprehensive reference tracks for each style"""
        references_data = {
            "Country": [
                ["Johnny Cash - Ring of Fire", "classic country anthem"],
                ["Dolly Parton - Jolene", "country ballad"],
                ["Willie Nelson - On the Road Again", "country road song"]
            ],
            "Funk": [
                ["James Brown - Sex Machine", "classic funk"],
                ["Parliament - Give Up the Funk", "P-funk classic"],
                ["Stevie Wonder - Superstition", "funky fusion"]
            ],
            "Blues": [
                ["B.B. King - The Thrill Is Gone", "classic blues ballad"],
                ["Stevie Ray Vaughan - Pride and Joy", "electric blues"],
                ["Muddy Waters - Mannish Boy", "blues standard"]
            ],
            "Classical": [
                ["Beethoven - Moonlight Sonata", "romantic piano"],
                ["Vivaldi - Four Seasons", "baroque classic"],
                ["Mozart - Eine kleine Nachtmusik", "classical symphony"]
            ],
            "Hip-Hop": [
                ["Dr. Dre - Nuthin' but a 'G' Thang", "west coast hip-hop"],
                ["Nas - NY State of Mind", "east coast hip-hop"],
                ["Tupac - Changes", "conscious hip-hop"]
            ],
            "Techno": [
                ["Jeff Mills - The Bells", "classic techno anthem"],
                ["Underworld - Born Slippy", "big beat techno"],
                ["Charlotte de Witte - Selected", "hard techno"]
            ],
            "Gospel": [
                ["Mahalia Jackson - Amazing Grace", "classic gospel"],
                ["Kirk Franklin - Hosanna", "contemporary gospel"],
                ["Aretha Franklin - Amazing Grace", "soulful gospel"]
            ],
            "Soul": [
                ["Marvin Gaye - What's Going On", "motown soul"],
                ["Aretha Franklin - Respect", "soul anthem"],
                ["Al Green - Let's Stay Together", "smooth soul"]
            ]
        }
        
        data = self.load_json("references.json")
        for style, refs in references_data.items():
            if style not in data:
                data[style] = refs
            else:
                # Merge new references
                for ref in refs:
                    if ref not in data[style]:
                        data[style].append(ref)
        
        self.save_json("references.json", data)
        print("✓ Expanded reference tracks")
    
    def add_advanced_emotions(self):
        """Add more nuanced emotions"""
        emotions_data = {
            "mysterious": {
                "keywords": ["mysterious", "enigmatic", "cryptic", "obscure", "神秘", "谜"],
                "description": "mysterious and enigmatic atmosphere"
            },
            "triumphant": {
                "keywords": ["triumphant", "victorious", "celebratory", "successful", "胜利", "凯旋"],
                "description": "triumphant and victorious atmosphere"
            },
            "contemplative": {
                "keywords": ["contemplative", "reflective", "meditative", "thoughtful", "沉思", "冥想"],
                "description": "contemplative and reflective mood"
            },
            "festive": {
                "keywords": ["festive", "celebratory", "party", "joyous", "节日", "庆祝"],
                "description": "festive and celebratory atmosphere"
            },
            "haunting": {
                "keywords": ["haunting", "eerie", "ethereal", "ghostly", "阴森", "诡异"],
                "description": "haunting and eerie feeling"
            }
        }
        
        data = self.load_json("emotions.json")
        added = 0
        for emotion, info in emotions_data.items():
            if emotion not in data:
                data[emotion] = info
                added += 1
        
        if added > 0:
            self.save_json("emotions.json", data)
            print(f"✓ Added {added} new emotions")
        else:
            print("No new emotions to add")
    
    def run_full_expansion(self):
        """Run complete data expansion"""
        print("=== Running Full Data Expansion ===\n")
        
        print("1. Adding musical styles...")
        self.add_musical_styles_from_wikipedia_genres()
        time.sleep(0.3)
        
        print("\n2. Adding emotions...")
        self.add_advanced_emotions()
        time.sleep(0.3)
        
        print("\n3. Adding reference tracks...")
        self.add_comprehensive_reference_tracks()
        
        print("\n✓ Data expansion complete!")

def main():
    expander = DataExpander()
    expander.run_full_expansion()
    
    print("\n=== Summary ===")
    print("Styles, emotions, and references have been expanded.")
    print("Run 'python data_loader.py' to verify the updated data.")
    print("Run 'python app.py' to test the expanded knowledge base!")

if __name__ == "__main__":
    main()

