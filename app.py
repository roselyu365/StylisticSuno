#!/usr/bin/env python3


# app.py
# Project: SonicPalette - terminal MVP (no AI)
# Author: you
# Description: Turn user description into Suno-style prompt components:
# styles, instruments, BPM, chord progressions, and reference tracks.

from dataclasses import dataclass, field
from typing import List, Dict, Tuple
import random
import textwrap

# -----------------------------
# Data Definitions (can be moved to JSON/CSV later)
# -----------------------------

EMOTION_KEYWORDS = {
    "warm": ["warm", "cozy", "gentle", "soft", "tender", "温暖", "温柔"],
    "chill": ["chill", "laid-back", "relaxed", "轻松", "慵懒", "lofi"],
    "melancholic": ["melancholy", "melancholic", "sad", "blue", "emo", "忧郁", "伤感"],
    "energetic": ["energetic", "upbeat", "driving", "punchy", "热血", "劲", "动感"],
    "dreamy": ["dreamy", "hazy", "shimmer", "airy", "朦胧", "梦幻"],
    "dark": ["dark", "moody", "noir", "阴郁", "冷峻"],
    "romantic": ["romantic", "intimate", "甜", "浪漫"],
    "nostalgic": ["nostalgic", "retro", "vintage", "怀旧", "复古"],
    "urban": ["urban", "city", "neon", "霓虹", "夜色", "城市"],
    "tropical": ["tropical", "island", "reggae", "阳光", "海风"]
}

# Style dictionary: keywords, bpm range, instruments, chord templates
STYLE_DB: Dict[str, Dict] = {
    "R&B": {
        "keywords": ["r&b", "soul", "neo-soul", "smooth", "silky", "urban", "late night", "柔滑"],
        "bpm": (70, 95),
        "instruments": ["Rhodes", "Electric piano", "Warm bass", "Soft kick & snare", "Silky synth pad", "Vocal layers"],
        "chords": [
            {"roman": "Imaj7 – vi7 – ii7 – V7", "C": "Cmaj7 – Am7 – Dm7 – G7"},
            {"roman": "ivmaj7 – V7 – iii7 – vi7", "C": "Fmaj7 – G7 – Em7 – Am7"},
            {"roman": "Imaj7 – iii7 – vi7 – ii7", "C": "Cmaj7 – Em7 – Am7 – Dm7"},
        ],
    },
    "Reggae": {
        "keywords": ["reggae", "dub", "tropical", "island", "sunny", "offbeat", "反拍", "牙买加"],
        "bpm": (60, 76),
        "instruments": ["Skank guitar (off-beat)", "Deep bass", "Dry drums", "Organ/Clav", "Spring reverb"],
        "chords": [
            {"roman": "I – V – vi – IV", "C": "C – G – Am – F"},
            {"roman": "ii – V – I", "C": "Dm – G – C"},
        ],
    },
    "Dream pop": {
        "keywords": ["dream pop", "shoegaze", "dreamy", "reverb", "浮游", "air", "hazy", "朦胧"],
        "bpm": (70, 95),
        "instruments": ["Shimmer guitar (reverb/delay)", "Airy pad", "Soft drums", "Chorus vocals", "Subtle synth"],
        "chords": [
            {"roman": "I – IV – Vsus – V", "C": "C – F – Gsus – G"},
            {"roman": "I – V – vi – IV", "C": "C – G – Am – F"},
        ],
    },
    "City pop": {
        "keywords": ["city pop", "retro", "80s", "japanese", "都会", "neon", "夜", "funky"],
        "bpm": (95, 115),
        "instruments": ["Electric guitar (clean)", "Slap/round bass", "Bright keys", "Disco hats", "Synth brass"],
        "chords": [
            {"roman": "Imaj7 – VI7 – ii7 – V7", "C": "Cmaj7 – A7 – Dm7 – G7"},
            {"roman": "Imaj7 – V/vi – vi – ii7 – V7", "C": "Cmaj7 – E7 – Am – Dm7 – G7"},
        ],
    },
    "Trip-hop": {
        "keywords": ["trip-hop", "moody", "noir", "downtempo", "vinyl", "阴郁", "港口雨夜"],
        "bpm": (70, 85),
        "instruments": ["Dusty drums", "Sub-bass", "Tape saturation", "Lo-fi keys", "Sparse samples"],
        "chords": [
            {"roman": "i – VI – III – VII (aeolian)", "C": "Am – F – C – G"},
            {"roman": "i – iv – v – i (minor)", "C": "Am – Dm – Em – Am"},
        ],
    },
    "Lo-fi hiphop": {
        "keywords": ["lofi", "study", "chill", "jazzy", "雨夜", "轻松"],
        "bpm": (65, 85),
        "instruments": ["Dusty drums", "Warm bass", "Rhodes", "Vinyl crackle", "Soft sax/keys"],
        "chords": [
            {"roman": "Imaj7 – vi7 – ii7 – V7", "C": "Cmaj7 – Am7 – Dm7 – G7"},
            {"roman": "ii7 – V7 – Imaj7", "C": "Dm7 – G7 – Cmaj7"},
        ],
    },
    "Synthwave": {
        "keywords": ["synthwave", "80s", "retro", "analog", "neon", "夜跑"],
        "bpm": (90, 110),
        "instruments": ["Analog polysynth", "Arp synth", "Gated reverb drums", "Punchy bass", "Chorus guitar"],
        "chords": [
            {"roman": "i – VI – III – VII (aeolian)", "C": "Am – F – C – G"},
            {"roman": "I – V – vi – IV", "C": "C – G – Am – F"},
        ],
    },
    "Post-rock": {
        "keywords": ["post-rock", "cinematic", "build-up", "延迟吉他", "层次", "情绪波峰"],
        "bpm": (80, 120),
        "instruments": ["Delay electric guitar", "Bass", "Drums (crescendo)", "Ambient pad", "Strings (optional)"],
        "chords": [
            {"roman": "I – IV – I – V (gradual build)", "C": "C – F – C – G"},
            {"roman": "vi – IV – I – V", "C": "Am – F – C – G"},
        ],
    },
    "Ambient": {
        "keywords": ["ambient", "drone", "space", "slow", "冥想", "空灵"],
        "bpm": (50, 80),
        "instruments": ["Evolving pads", "Texture drones", "Piano sparsely", "Field recordings", "Granular beds"],
        "chords": [
            {"roman": "I – IV – I (sustain)", "C": "C – F – C"},
            {"roman": "I – ii – I (modal)", "C": "C – Dm – C"},
        ],
    },
}

# Reference track mini library (style -> list of tuples: (artist - title, note))
REFERENCE_DB: Dict[str, List[Tuple[str, str]]] = {
    "R&B": [
        ("The Weeknd - Earned It", "silky, urban R&B ballad"),
        ("FKJ - Tadow", "neo-soul, Rhodes & smooth bass"),
        ("Daniel Caesar - Best Part", "intimate R&B duet"),
    ],
    "Reggae": [
        ("Bob Marley - No Woman, No Cry", "classic roots reggae"),
        ("Toots & The Maytals - 54-46", "ska/rocksteady edge"),
        ("Rhye - Taste (reggae remix vibe)", "modern mellow twist"),
    ],
    "Dream pop": [
        ("Beach House - Space Song", "iconic hazy dream pop"),
        ("Alvvays - Dreams Tonite", "bright, nostalgic tint"),
        ("M83 - Midnight City", "synth-lush dreaminess"),
    ],
    "City pop": [
        ("Tatsuro Yamashita - Sparkle", "city pop gold"),
        ("Miki Matsubara - Stay With Me", "classic vibe"),
        ("落日飞车 Sunset Rollercoaster - My Jinji", "modern city-pop adjacent"),
    ],
    "Trip-hop": [
        ("Massive Attack - Teardrop", "moody, iconic trip-hop"),
        ("Portishead - Roads", "noir, cinematic"),
        ("Tricky - Hell Is Round The Corner", "dark texture"),
    ],
    "Lo-fi hiphop": [
        ("J Dilla - Donuts (various)", "lo-fi crate-digging vibe"),
        ("Nujabes - Feather", "jazzy chill"),
        ("Jinsang - affection", "classic lofi study"),
    ],
    "Synthwave": [
        ("Kavinsky - Nightcall", "retro analog mood"),
        ("Timecop1983 - On the Run", "romantic synthwave"),
        ("The Midnight - Sunset", "modern synthwave"),
    ],
    "Post-rock": [
        ("Explosions in the Sky - Your Hand in Mine", "build & catharsis"),
        ("Mono - Ashes in the Snow", "cinematic swell"),
        ("Wang Wen 惘闻 - Red Wall and Black Wall", "Chinese post-rock"),
    ],
    "Ambient": [
        ("Brian Eno - An Ending (Ascent)", "pioneering ambient"),
        ("Stars of the Lid - Requiem for Dying Mothers", "drone beauty"),
        ("Hammock - Turn Away and Return", "lush ambient"),
    ],
    # Optional: specific Chinese indie reference you mentioned
    "Indie refs": [
        ("黑裙子 - lingling", "Chinese indie electronic/alt reference"),
    ]
}

# Cross-emotion to style nudges (adds small weights)
EMOTION_TO_STYLES = {
    "warm": {"R&B": 0.4, "Lo-fi hiphop": 0.3, "City pop": 0.2},
    "chill": {"Lo-fi hiphop": 0.4, "Dream pop": 0.3, "Ambient": 0.2},
    "melancholic": {"Trip-hop": 0.4, "Dream pop": 0.3, "Post-rock": 0.2},
    "energetic": {"City pop": 0.3, "Synthwave": 0.3, "Post-rock": 0.2},
    "dreamy": {"Dream pop": 0.5, "Ambient": 0.3, "Post-rock": 0.1},
    "dark": {"Trip-hop": 0.5, "Synthwave": 0.2, "Ambient": 0.2},
    "romantic": {"R&B": 0.4, "City pop": 0.3, "Dream pop": 0.2},
    "nostalgic": {"City pop": 0.4, "Synthwave": 0.3, "Lo-fi hiphop": 0.2},
    "urban": {"R&B": 0.4, "Trip-hop": 0.3, "Lo-fi hiphop": 0.2},
    "tropical": {"Reggae": 0.6, "City pop": 0.2},
}

# -----------------------------
# Core logic
# -----------------------------

def tokenize(s: str) -> List[str]:
    s = s.lower()
    tokens = []
    # naive tokenizer: split by non-alphabetic, keep CJK as-is
    buf = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            buf += ch
        else:
            if buf:
                tokens.append(buf)
                buf = ""
            if '\u4e00' <= ch <= '\u9fff':
                tokens.append(ch)
    if buf:
        tokens.append(buf)
    return tokens

def match_emotions(tokens: List[str]) -> List[str]:
    hits = []
    for emo, kws in EMOTION_KEYWORDS.items():
        if any(kw.lower() in tokens for kw in [k for k in kws if k.isascii()]) or any(k in tokens for k in [k for k in kws if not k.isascii()]):
            hits.append(emo)
    return hits or ["chill"]  # default

def compute_style_scores(tokens: List[str], emotions: List[str]) -> Dict[str, float]:
    scores = {style: 0.0 for style in STYLE_DB.keys()}
    # keyword matches
    for style, meta in STYLE_DB.items():
        for kw in meta["keywords"]:
            if kw.isascii():
                if kw.lower() in tokens:
                    scores[style] += 1.0
            else:
                if kw in tokens:
                    scores[style] += 1.0
    # emotion nudges
    for emo in emotions:
        for style, w in EMOTION_TO_STYLES.get(emo, {}).items():
            scores[style] += w
    # small bonus for explicit words like "slow/fast/retro/modern"
    if "retro" in tokens or "复古" in tokens:
        scores["City pop"] += 0.3
        scores["Synthwave"] += 0.3
    if "modern" in tokens or "现代" in tokens:
        scores["R&B"] += 0.2
        scores["Indie"] = scores.get("Indie", 0) + 0.2  # harmless extra key
    return scores

def pick_top_styles(scores: Dict[str, float], k: int = 2) -> List[str]:
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top = [name for name, sc in ranked if sc > 0]
    if not top:
        # default blend
        return ["R&B", "Dream pop"]
    return top[:k]

def blend_bpm(styles: List[str]) -> Tuple[int, int]:
    lows, highs = [], []
    for st in styles:
        b = STYLE_DB[st]["bpm"]
        lows.append(b[0]); highs.append(b[1])
    # take midpoint of mins and maxs to get an overlapping suggestion
    low = int(sum(lows)/len(lows))
    high = int(sum(highs)/len(highs))
    if low >= high:
        low, high = min(lows), max(highs)
    return (low, high)

def collect_instruments(styles: List[str]) -> List[str]:
    bank = []
    for st in styles:
        bank.extend(STYLE_DB[st]["instruments"])
    # de-duplicate while keeping order
    seen = set()
    result = []
    for it in bank:
        if it not in seen:
            seen.add(it)
            result.append(it)
    # cap to ~8
    return result[:8]

def pick_chords(styles: List[str], n: int = 2) -> List[Dict[str, str]]:
    pool = []
    for st in styles:
        pool.extend(STYLE_DB[st]["chords"])
    random.shuffle(pool)
    # de-duplicate by roman
    seen = set()
    out = []
    for ch in pool:
        if ch["roman"] not in seen:
            out.append(ch)
            seen.add(ch["roman"])
        if len(out) >= n:
            break
    return out

def suggest_references(styles: List[str], emotions: List[str], n: int = 5) -> List[Tuple[str, str]]:
    pool = []
    for st in styles:
        pool.extend(REFERENCE_DB.get(st, []))
    # add indie references occasionally
    pool.extend(REFERENCE_DB.get("Indie refs", []))
    random.shuffle(pool)
    # ensure diversity
    out = []
    seen = set()
    for item in pool:
        if item[0] not in seen:
            out.append(item)
            seen.add(item[0])
        if len(out) >= n:
            break
    return out


def word_count(s: str) -> int:
    return len(s.split())

def build_prompt_sections(styles, emotions, bpm_range, instruments):
    style_str = " + ".join(styles)
    emo_words = ", ".join(emotions)
    bpm_str = f"{bpm_range[0]}–{bpm_range[1]} BPM"
    instr_str = ", ".join(instruments)

    # 基础标签
    base_style = f"{style_str} style"
    base_mood = f"{emo_words} mood"
    base_instr = f"instrumentation: {instr_str}"

    # groove：长/短两档
    groove_long = "groove: subtle swing, tasteful syncopation"
    groove_short = "groove: light swing, syncopation"

    # mix：根据情绪动态取集合，支持长/短两档
    mix_tags = ["warm", "silky", "tape saturation", "room reverb", "sidechain", "wide stereo"]
    if "dark" in emotions:
        mix_tags = ["moody", "noir", "tape saturation", "tight room", "mono bass focus"]
    if "energetic" in emotions and "punchy drums" not in mix_tags:
        mix_tags = mix_tags[:5] + ["punchy drums"]

    mix_long = "mix: " + ", ".join(mix_tags[:6])
    mix_short = "mix: " + ", ".join(mix_tags[:4])

    tempo_line = f"tempo: {bpm_str}"

    # structure：长/短两档
    structure_long = "structure: intro – verse – chorus – verse – bridge – outro"
    structure_short = "structure: intro–verse–chorus–bridge–outro"

    # chords：两种呈现方式（主prompt极简+详细移到末尾回显）
    # 在主prompt内放“罗马数字极简句”，并在终端下方仍打印详细chords列表（你已有逻辑）
    chords_inline = None  # 默认为不放在主句，如你想强制包含，可用短语版：
    # chords_inline = "chords: diatonic pop/jazz cycles"

    sections = [
        {"name": "style",     "hard": f"{base_style}",          "soft": None,               "prio": 1},
        {"name": "mood",      "hard": f"{base_mood}",           "soft": None,               "prio": 1},
        {"name": "instr",     "hard": f"{base_instr}",          "soft": None,               "prio": 1},
        {"name": "groove",    "hard": groove_long,              "soft": groove_short,       "prio": 2},
        {"name": "mix",       "hard": mix_long,                 "soft": mix_short,          "prio": 2},
        {"name": "tempo",     "hard": tempo_line,               "soft": None,               "prio": 1},
        {"name": "structure", "hard": structure_long,           "soft": structure_short,    "prio": 3},
    ]

    if chords_inline:
        sections.append({"name": "chords", "hard": chords_inline, "soft": None, "prio": 2})

    return sections

def compress_sections(sections, max_words=200, delimiter="; "):
    # 第一轮：使用所有 hard 版本
    parts = [s["hard"] for s in sections if s["hard"]]
    text = delimiter.join(parts) + "."
    if word_count(text) <= max_words:
        return text

    # 第二轮：尝试将可降级的部分切换到 soft 版本（按优先级从低到高切）
    # prio数值越大越容易被压缩
    for prio in sorted(set(s["prio"] for s in sections)):
        for i, s in enumerate(sections):
            if s["prio"] == prio and s.get("soft"):
                parts = []
                for j, sj in enumerate(sections):
                    if j == i and sj.get("soft"):
                        parts.append(sj["soft"])
                    else:
                        parts.append(sj["hard"] or "")
                text_try = delimiter.join([p for p in parts if p]) + "."
                if word_count(text_try) <= max_words:
                    return text_try
                else:
                    # 保留这个降级，继续尝试其它可降级项
                    sections[i]["hard"] = sections[i]["soft"]

    # 第三轮：在仍超长的情况下，对冗长列表做轻量精简（只针对 instr 和 mix）
    def shorten_list_line(line, keep=4):
        # 针对 "instrumentation: a, b, c, d, e, f" 或 "mix: a, b, c, d, e, f"
        if ":" not in line:
            return line
        head, tail = line.split(":", 1)
        items = [x.strip() for x in tail.split(",")]
        if len(items) <= keep:
            return line
        short = ", ".join(items[:keep]) + ", etc."
        return f"{head.strip()}: {short}"

    for target in ["instr", "mix"]:
        idx = next((i for i, s in enumerate(sections) if s["name"] == target), None)
        if idx is not None and sections[idx]["hard"]:
            sections[idx]["hard"] = shorten_list_line(sections[idx]["hard"], keep=4)

    parts = [s["hard"] for s in sections if s["hard"]]
    text = delimiter.join(parts) + "."
    if word_count(text) <= max_words:
        return text

    # 第四轮：作为兜底，将 delimiter 从 "; " 改为 ", "，以减少词数开销
    text = ", ".join(parts) + "."
    # 再次检查
    if word_count(text) > max_words:
        # 最后的安全阀：逐词裁剪，但保证每个模块至少保留头部5个词
        # 拼接时记录每段词数，尽量均匀裁
        tokens_by_part = [p.split() for p in parts]
        total = sum(len(t) for t in tokens_by_part)
        if total <= max_words:
            return " ".join(" ".join(t) for t in tokens_by_part)

        # 目标：保底每段至少5词
        min_part = 5
        while total > max_words:
            # 找到当前最长的段且长度>min_part，削减1词
            lengths = [len(t) for t in tokens_by_part]
            i = max(range(len(lengths)), key=lambda k: lengths[k])
            if lengths[i] > min_part:
                tokens_by_part[i].pop()  # 去掉最后一个词
                total -= 1
            else:
                # 如果都已经到保底，退出（极端情况下可能略超）
                break
        text = " ".join(" ".join(t) for t in tokens_by_part)
    return text

def format_suno_prompt(styles, emotions, bpm_range, instruments) -> str:
    sections = build_prompt_sections(styles, emotions, bpm_range, instruments)
    prompt = compress_sections(sections, max_words=200)
    return prompt


@dataclass
class UserIntent:
    description: str
    tempo_pref: str = "auto"
    texture_pref: str = "auto"
    era_pref: str = "auto"

def apply_prefs(bpm_range: Tuple[int, int], instruments: List[str], intent: UserIntent) -> Tuple[Tuple[int,int], List[str]]:
    low, high = bpm_range
    if intent.tempo_pref == "slow":
        low, high = max(50, low-10), max(55, low+5)
    elif intent.tempo_pref == "fast":
        low, high = min(high+5, 140), min(high+15, 150)
    # texture preference: push instruments set lightly
    if intent.texture_pref == "electronic":
        bonus = ["Analog polysynth", "Arp synth", "Silky synth pad", "Sub-bass"]
        instruments = list(dict.fromkeys(instruments + bonus))[:8]
    elif intent.texture_pref == "acoustic":
        bonus = ["Electric guitar (clean)", "Piano", "Strings", "Bass", "Drums"]
        instruments = list(dict.fromkeys(bonus + instruments))[:8]
    return (low, high), instruments

# -----------------------------
# CLI flow
# -----------------------------

def main():
    print("=== SonicPalette: Suno Prompt Builder (Terminal MVP) ===")
    desc = input("1) Describe the vibe/scene/emotion (自由描述，可中英混合):\n> ").strip()
    if not desc:
        print("No description provided. Exiting.")
        return

    print("\n2) Tempo preference? [auto/slow/medium/fast] (回车默认 auto)")
    tempo = input("> ").strip().lower() or "auto"
    if tempo not in ["auto","slow","medium","fast"]:
        tempo = "auto"

    print("\n3) Texture preference? [auto/electronic/acoustic] (回车默认 auto)")
    texture = input("> ").strip().lower() or "auto"
    if texture not in ["auto","electronic","acoustic"]:
        texture = "auto"

    print("\n4) Era preference? [auto/retro/modern] (回车默认 auto)")
    era = input("> ").strip().lower() or "auto"
    if era not in ["auto","retro","modern"]:
        era = "auto"

    intent = UserIntent(description=desc, tempo_pref=tempo, texture_pref=texture, era_pref=era)

    tokens = tokenize(intent.description)
    emotions = match_emotions(tokens)
    scores = compute_style_scores(tokens, emotions)
    top_styles = pick_top_styles(scores, k=2)
    bpm_range = blend_bpm(top_styles)
    instruments = collect_instruments(top_styles)
    chords = pick_chords(top_styles, n=2)
    bpm_range, instruments = apply_prefs(bpm_range, instruments, intent)
    refs = suggest_references(top_styles, emotions, n=5)
    prompt = format_suno_prompt(top_styles, emotions, bpm_range, instruments)

    print("\n--- RESULT ---")
    print(f"Styles: {', '.join(top_styles)}")
    print(f"Emotions: {', '.join(emotions)}")
    print(f"BPM suggestion: {bpm_range[0]}–{bpm_range[1]}")
    print("\nSuno-style prompt:")
    print(textwrap.fill(prompt, width=100))

    print("\nChord progressions (Roman / C example):")
    for ch in chords:
        print(f"- {ch['roman']}  |  e.g., {ch['C']}")

    print("\nInstrumentation suggestions:")
    for it in instruments:
        print(f"- {it}")

    print("\nReference tracks:")
    for a, note in refs:
        print(f"- {a}  — {note}")

    print("\nCopy the prompt above into Suno. You can rerun and tweak preferences to iterate quickly.")
    print("=========================================================")

if __name__ == "__main__":
    main()