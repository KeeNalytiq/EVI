# EVI

**EVI — Your life. Your vision. Your AI.**

EVI is an AI-powered personal companion designed to help people understand what they want, turn goals into practical plans, build consistent habits, reflect on progress, and take meaningful action.

The long-term product vision is a permission-aware personal AI system that can coordinate conversation, memory, goals, planning, and approved actions — while keeping the user in control.

## Current status

This repository contains the first production-oriented foundation:

- Python + FastAPI backend
- Ollama local inference
- Configurable open-weight LLM (Qwen3.5 by default)
- Conversation API
- Health endpoint
- CORS configuration
- Environment-based configuration
- Clean separation between API, AI, and configuration layers

## Architecture

```
Client / Frontend
       |
       v
 FastAPI API
       |
       v
 EVI Orchestrator
       |
       +---- Conversation / Context
       |
       +---- Memory Engine       (next)
       |
       +---- Goal Engine         (next)
       |
       +---- Planning Engine     (next)
       |
       +---- Action Engine       (next)
       |
       v
 Ollama
       |
       v
 Local Open-Weight LLM
```

## Local development

### 1. Requirements

- Python 3.11+
- Ollama
- A local model supported by Ollama

### 2. Start Ollama

Install Ollama from the official website and pull the configured model.

Example:

```bash
ollama pull qwen3.5:2b
```

### 3. Start the backend

```cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

### 4. Test

Health:

```bash
curl http://127.0.0.1:8000/health
```

Chat:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Help me plan my week."}'
```

## Product principles

1. **User agency first** — EVI assists; it does not silently take control.
2. **Permission-aware actions** — external actions will require appropriate authorization.
3. **Private by design** — local inference is the default development path.
4. **Useful memory** — remember what helps the user, not everything indiscriminately.
5. **Action over empty motivation** — convert intentions into realistic next steps.
6. **Safety boundaries** — high-stakes medical, legal, and financial decisions require appropriate professional support.

## Roadmap

- [x] EVI backend foundation
- [x] Local LLM integration
- [x] Chat API
- [ ] Conversation persistence
- [ ] Personal memory engine
- [ ] User profile
- [ ] Vision and goals engine
- [ ] Habit and discipline engine
- [ ] Planning engine
- [ ] Action/automation engine
- [ ] Web/mobile frontend
- [ ] Authentication and multi-user support
- [ ] Observability and evaluation
- [ ] Production deployment

## License

TBD while the project architecture and licensing strategy are being finalized.
