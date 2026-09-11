# WaterPulse AI Agent V8.5

V8.5 is the deployment-hardening release.

- Same V8.3/V8.4 user experience and analysis flow.
- Designed to survive GitHub web-upload folder flattening.
- `bootstrap_layout.py` rebuilds `tools/`, `agent/`, `core/`, `engines/`, `static/`, `data/`, and `qa/golden/` inside Railway before the app imports.
- DeepSeek key is read only from Railway environment variables.
- Health endpoint: `/api/health`.
- DeepSeek live test: `/api/deepseek/test`.
- Field contract QA: `/api/data-contract`.

See `DEPLOY_V8_5.md`.
