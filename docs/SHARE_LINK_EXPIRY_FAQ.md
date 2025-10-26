# Share Link Expiry FAQ

## The Message You See

```
Running on public URL: https://xxxxxx.gradio.live
* Link expires in 72 hours
```

## Is This Normal?

✅ **YES!** This is expected behavior.

## Why Does It Expire?

Gradio's free share link feature creates a temporary tunnel. It's designed for:
- Quick demos and testing
- Temporary sharing with others
- Not for permanent production use

## What Are Your Options?

### 1. Use Local URL (Never Expires)

The local URL `http://127.0.0.1:7860` works permanently for you:
- ✅ Never expires
- ✅ Private
- ✅ No internet needed after loading
- ❌ Only accessible on your computer

### 2. Get a New Link Every 72 Hours

Just re-run:
```bash
python gradio_ui.py
```

Gets a new shareable link.

### 3. Deploy to Hugging Face (Free, Permanent)

Best for production:
1. Create account at https://huggingface.co
2. Create Space
3. Upload your code
4. Get permanent URL like `username-appname.hf.space`

### 4. Use Gradio Paid Plan

For business use:
- ~$10/month
- Permanent links
- No code changes needed

## Quick Fixes

### Make It Not Expire (Local Only)

Change line 64 in `gradio_ui.py`:
```python
demo.launch(share=False)  # Change from True to False
```

Then run:
```bash
python gradio_ui.py
```

Local URL `http://127.0.0.1:7860` never expires!

### Keep Share Link (Temporary)

Keep using:
```bash
python gradio_ui.py
```

Just re-run every 72 hours to get a new link.

## Summary

| Option | Duration | Cost | Access |
|--------|----------|------|--------|
| Local URL | Forever | Free | You only |
| Share link | 72 hours | Free | Public |
| Hugging Face | Forever | Free | Public |
| Gradio Paid | Forever | ~$10/mo | Public |

## Recommendation

For your project:

**Development/Personal Use:**
```bash
python gradio_ui.py  # Use local URL, never expires
```

**Sharing with Others:**
```bash
python gradio_ui.py  # Get new link when current one expires
```

**Production:**
Deploy to Hugging Face Spaces (free, permanent, public)

## Bottom Line

The 72-hour expiration is **intentional** - not a bug! It encourages proper deployment for production while allowing quick sharing for demos.

Your local URL at `http://127.0.0.1:7860` **never expires** and works perfectly for personal use! 🎉

