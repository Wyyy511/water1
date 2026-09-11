from __future__ import annotations
import os, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from bootstrap_layout import ensure_layout
info = ensure_layout()
print("[WaterPulse V8.5] deployment layout ready:", info, flush=True)

# Verify the real application can import BEFORE binding the port.
import server  # noqa: F401
print("[WaterPulse V8.5] server import OK", flush=True)

import uvicorn
port = int(os.getenv("PORT", "8080"))
uvicorn.run("server:app", host="0.0.0.0", port=port, app_dir=str(ROOT), log_level="info")
