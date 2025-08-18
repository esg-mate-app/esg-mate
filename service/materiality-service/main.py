from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .controllers.materiality_controller import router as materiality_router
import os

app = FastAPI(
    title="Materiality Service",
    description="Materiality Assessment Service",
    version="1.0.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(materiality_router, tags=["materiality"])

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8002))
    uvicorn.run(app, host="0.0.0.0", port=port)
