from yt_dlp import YoutubeDL


def get_youtube_metadata(url: str):

    ydl_opts = {
        "quiet": True,
        "extract_flat": False
    }

    with YoutubeDL(ydl_opts) as ydl:

        info = ydl.extract_info(
            url,
            download=False
        )

    views = info.get("view_count") or 0
    likes = info.get("like_count") or 0
    comments = info.get("comment_count") or 0

    engagement_rate = 0

    if views > 0:
        engagement_rate = (
            (likes + comments)
            / views
        ) * 100

    return {
        "video_id": info.get("id"),
        "title": info.get("title"),
        "creator": info.get("uploader"),
        "views": views,
        "likes": likes,
        "comments": comments,
        "engagement_rate": round(
            engagement_rate,
            4
        ),
        "duration": info.get("duration"),
        "upload_date": info.get("upload_date"),
        "thumbnail": info.get("thumbnail"),
        "description": info.get("description")
    }