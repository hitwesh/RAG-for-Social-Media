from pydantic import BaseModel


class VideoAnalyzeRequest(BaseModel):
    youtube_url: str
    instagram_url: str