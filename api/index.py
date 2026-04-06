from fastapi import FastAPI
from app.routes import analyze, stream, state

app = FastAPI()

# 라우터 등록
app.include_router(analyze.router)
app.include_router(stream.router)
app.include_router(state.router)


@app.get("/health")
def health():
    return {"status": "ok"}