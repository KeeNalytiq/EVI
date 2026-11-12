# EVI Architecture

## Phase 1 — Local AI foundation

```
Frontend
   |
   v
FastAPI
   |
   +--> Conversation API
   |
   +--> EVI Orchestrator
   |
   v
Ollama
   |
   v
Open-weight LLM
```

## Phase 2 — Personal intelligence

The backend will add explicit services for:

- User profile
- Personal memory
- Goals and life vision
- Habits
- Planning
- Reflection
- Context retrieval

The important design decision is to keep these capabilities as separate domain services instead of putting everything into one giant prompt.

## Phase 3 — Action system

EVI will eventually expose permission-aware tools such as:

- Calendar operations
- Reminders
- Email drafting/sending
- Task management
- Web research
- Other integrations

Actions should be represented as structured tool calls and validated before execution. Destructive, financial, external-communication, or otherwise consequential actions should require appropriate user confirmation.

## Data flow

```
User message
    |
    v
Context assembly
    |
    +--> recent conversation
    +--> relevant memory
    +--> active goals
    +--> current plan
    |
    v
LLM reasoning
    |
    +--> direct response
    +--> structured intent/tool request
    |
    v
Response / approved action
```

This architecture is intentionally incremental: EVI starts useful with a local model, then grows into a personal intelligence platform.
