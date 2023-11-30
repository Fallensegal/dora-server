from fastapi import FastAPI

app = FastAPI()

@app.get("/healthz")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
