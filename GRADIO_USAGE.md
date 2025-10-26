# Gradio Usage Guide

## Overview

The Gradio web interface has different launch options depending on your needs.

## Launch Options

### 1. Local Only (Default, No Expiration)

```bash
python gradio_ui.py
```

**Benefits:**
- ✅ Never expires
- ✅ Private - only accessible on your computer
- ✅ No internet required (after first load)

**Access:** Only at `http://127.0.0.1:7860` on your machine

### 2. Shareable Link (Temporary, 72 Hours)

```bash
python gradio_ui.py --share
# or short form
python gradio_ui.py -s
```

**Benefits:**
- ✅ Share with others
- ✅ Access from anywhere
- ✅ Public URL provided

**Limitations:**
- ⏰ Link expires in 72 hours
- 📊 Rate limited (but reasonable for normal use)

### 3. Permanent Shareable Link

For a permanent link (no expiration), you need Gradio's paid plan:

1. Sign up at https://gradio.app
2. Get an API key
3. Install with auth: `demo.launch(share=True, auth=("your_username", "your_password"))`

**Cost:** ~$10/month for permanent links

## About the Expiration

### Why It Expires?

Gradio creates temporary tunnels for the share feature to make your local app accessible online without complex networking setup.

### Default Behavior
- **Local URL**: `http://127.0.0.1:7860` - Never expires, private
- **Share link**: Expires in 72 hours (free tier)
- **Paid plan**: Permanent links available

### When Link Expires

After 72 hours:
1. Just relaunch with `--share` to get a new link
2. Share the new link with users
3. Or use the local URL which never expires

## Usage Scenarios

### Scenario 1: Local Development
```bash
# No share flag - private, permanent
python gradio_ui.py
```
Best for: Personal use, development, testing

### Scenario 2: Share with Friends/Colleagues
```bash
# With share flag - temporary link
python gradio_ui.py --share
```
Best for: Quick demos, temporary sharing, testing with others

### Scenario 3: Production Deployment
Use hosting options:
- Deploy to Hugging Face Spaces (free, permanent)
- Use Gradio paid plan
- Self-host with ngrok or similar

## Upgrading to Permanent Link

### Option 1: Hugging Face Spaces (Free!)

1. Create account at https://huggingface.co
2. Create a new Space
3. Upload your code
4. Gets permanent URL like `username-appname.hf.space`

### Option 2: Gradio Paid Plan

1. Sign up at https://gradio.app
2. ~$10/month for permanent links
3. No code changes needed

### Option 3: Self-Hosting

Use tunneling services:
- ngrok
- Cloudflare Tunnel
- LocalTunnel

## Current Status

Your current link expires in 72 hours. Options:

**Immediate:**
- Just re-run with `--share` to get new link
- Or use local URL: `http://127.0.0.1:7860`

**Long-term:**
- Deploy to Hugging Face (free, permanent)
- Use Gradio paid plan (~$10/month)
- Keep using local URL (free, permanent for you)

## Quick Commands

```bash
# Local only (permanent, private)
python gradio_ui.py

# Shareable (expires in 72h)
python gradio_ui.py --share

# Check help
python gradio_ui.py --help
```

## Access URLs

**Local URL** (never expires):
- Only accessible on your computer
- URL: `http://127.0.0.1:7860`

**Share Link** (expires in 72h):
- Accessible from anywhere
- URL: `https://xxxxxx.gradio.live`
- Shows: "Link expires in 72 hours"

## Why This Design?

Gradio provides the share feature as a convenience for quick demos and testing. For production use, they expect you to:
1. Deploy properly (Hugging Face Spaces)
2. Use paid plans for permanent links
3. Or use the local URL for personal use

This is standard practice - temporary free links for sharing, permanent solutions for production.

## Summary

✅ **Your local URL works forever** - No expiration  
⏰ **Share links expire** - After 72 hours  
🔄 **Easy renewal** - Just re-run `--share`  
🚀 **Production options** - Hugging Face Spaces (free) or paid plans  

The expiration is not a bug - it's intentional to encourage proper deployment for production use while allowing quick sharing for demos!

