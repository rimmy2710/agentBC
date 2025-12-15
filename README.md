# news-agent-poc

This proof-of-concept scaffolds a small Python package with a minimal OpenAI Responses API smoke test.

## Prerequisites
- Python 3.11+
- An OpenAI API key with access to the Responses API

## Setup and usage
1. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Copy the environment template and add your OpenAI API key:
   ```bash
   cp .env.example .env
   echo "OPENAI_API_KEY=sk-..." >> .env
   ```
3. Run the smoke test:
   ```bash
   python -m src.news_agent.main
   ```

### Convenience script
You can also run everything with the helper script:
```bash
bash scripts/run_local.sh
```

The script creates a virtual environment, installs dependencies, and runs the smoke test.
