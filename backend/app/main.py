from fastapi import FastAPI

from app.api.video_routes import router


app = FastAPI()


app.include_router(
    router,
    prefix="/videos",
    tags=["Videos"]
)


@app.get("/")
def root():
    return {
        "status": "ok"
    }