# WaterPulse V8.5 — Railway flat-upload-safe deployment

This package is intentionally FLAT. That is deliberate.

## Why
GitHub's web upload flattened your previous folder structure, so Railway saw:
`data_tool.py`, `router.py`, `index.html` at repository root instead of `tools/`, `agent/`, `static/`.
V8.5 reconstructs the required folders automatically at container startup.

## Upload
1. Unzip this V8.5 package.
2. Upload **all files inside it** to the GitHub repository root.
3. Do not create `tools/`, `agent/`, `core/`, `engines/`, `static/`, `data/` yourself.
4. Railway → Redeploy latest commit.

## DeepSeek
In Railway → Service → Variables:
- `DEEPSEEK_API_KEY` = your NEW/rotated DeepSeek key
- `DEEPSEEK_MODEL` = `deepseek-v4-flash`

Do NOT put the key in GitHub files.

## Verify
Open:
- `/api/health` → must show `"version":"8.5"` and `"deployment_layout":"flat-upload-safe"`
- `/api/deepseek/test` → after the key is set, should show `ok: true`
- `/api/data-contract` → should show 51 fields / 10 gaps

If `/api/health` shows 8.5, the folder-flattening problem is fixed.
