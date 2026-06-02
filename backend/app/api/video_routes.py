from fastapi import APIRouter

from app.schemas.video_schema import (
    VideoAnalyzeRequest
)

from app.services.youtube_service import (
    get_youtube_metadata
)

router = APIRouter()


@router.post("/analyze")
def analyze_video(
    payload: VideoAnalyzeRequest
):

    youtube_data = get_youtube_metadata(
        payload.youtube_url
    )

    return {
        "youtube": youtube_data
    }