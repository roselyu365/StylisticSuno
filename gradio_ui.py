import gradio as gr
from app import (
    tokenize, match_emotions, compute_style_scores, pick_top_styles,
    blend_bpm, collect_instruments, pick_chords, suggest_references,
    format_suno_prompt, apply_prefs, UserIntent
)

print("Loaded UserIntent:", UserIntent, type(UserIntent), flush=True)

def generate(desc, tempo_pref, texture_pref, era_pref):
    intent = UserIntent(description=desc, tempo_pref=tempo_pref, texture_pref=texture_pref, era_pref=era_pref)
    if not desc or not desc.strip():
        return "Please enter a description.", "", "", "", ""
    tokens = tokenize(desc)
    emotions = match_emotions(tokens)
    scores = compute_style_scores(tokens, emotions)
    top_styles = pick_top_styles(scores, 2)
    bpm_range = blend_bpm(top_styles)
    instruments = collect_instruments(top_styles)
    chord_list = pick_chords(top_styles, 2)
    bpm_range, instruments = apply_prefs(bpm_range, instruments, intent)
    refs = suggest_references(top_styles, emotions, 5)
    prompt = format_suno_prompt(top_styles, emotions, bpm_range, instruments)

    meta = f"Styles: {', '.join(top_styles)}\nEmotions: {', '.join(emotions)}\nBPM: {bpm_range[0]}–{bpm_range[1]}\nTempo: {tempo_pref}, Texture: {texture_pref}, Era: {era_pref}"
    chords_txt = "\n".join([f"- {c['roman']} | e.g., {c['C']}" for c in chord_list])
    instr_txt = "\n".join([f"- {i}" for i in instruments])
    refs_txt = "\n".join([f"- {a} — {note}" for a, note in refs])
    return prompt, meta, chords_txt, instr_txt, refs_txt

with gr.Blocks(theme=gr.themes.Soft(primary_hue="indigo", secondary_hue="blue")) as demo:
    gr.Markdown("## SonicPalette — Suno Prompt Builder")
    with gr.Row():
        with gr.Column(scale=3):
            in_desc = gr.Textbox(label="Describe your vibe", lines=4, placeholder="e.g., Neon city at night, slightly melancholic yet hopeful, dreamy glitchy electronic")
            with gr.Row():
                in_tempo = gr.Dropdown(choices=["auto","slow","medium","fast"], value="auto", label="Tempo")
                in_texture = gr.Dropdown(choices=["auto","electronic","acoustic"], value="auto", label="Texture")
                in_era = gr.Dropdown(choices=["auto","retro","modern"], value="auto", label="Era")
            run_btn = gr.Button("Generate Prompt", variant="primary")
        with gr.Column(scale=2):
            out_prompt = gr.Textbox(label="Suno-style Prompt", lines=8)
            out_meta = gr.Textbox(label="Meta", lines=6)
            out_chords = gr.Textbox(label="Chord progressions", lines=6)
            out_instr = gr.Textbox(label="Instrumentation", lines=6)
            out_refs = gr.Textbox(label="Reference tracks", lines=6)
    run_btn.click(generate, inputs=[in_desc, in_tempo, in_texture, in_era], outputs=[out_prompt, out_meta, out_chords, out_instr, out_refs])

if __name__ == "__main__":
    print("Launching Gradio...", flush=True)
    demo.launch(share=True)
