# Deployment Guide

## Streamlit Community Cloud (Recommended)
1. Push repo to GitHub.
2. New app → pick repo/branch → main file: `app/app.py`.
3. If weights are not committed, set a secret:
   ```yaml
   MODEL_URL: "https://drive.google.com/uc?id=<FILE_ID>&export=download"
   ```
4. App boots and caches weights on first run.
