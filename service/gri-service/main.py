from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .controllers.gri_controller import router as gri_router
import os

app = FastAPI(
    title="GRI Service",
    description="GRI Standards Service",
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
app.include_router(gri_router, tags=["gri"])

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8003))
    uvicorn.run(app, host="0.0.0.0", port=port)
