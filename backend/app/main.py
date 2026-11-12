from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .ai import OllamaError, chat
from .config import get_settings
from .models import ChatRequest, ChatResponse


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    description="EVI personal AI companion backend",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok", "service": "EVI"}


@app.post(f"{settings.api_prefix}/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest) -> ChatResponse:
    try:
        response = await chat(
            message=request.message,
            history=[item.model_dump() for item in request.history],
        )
    except OllamaError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc

    return ChatResponse(
        response=response,
        model=settings.ollama_model,
    )
