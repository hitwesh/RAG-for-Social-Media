from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime
from sqlalchemy import Text

from app.db.base import Base


class Video(Base):

    __tablename__ = "videos"

    id = Column(Integer, primary_key=True)

    platform = Column(String, nullable=False)

    platform_video_id = Column(
        String,
        unique=True
    )

    url = Column(String)

    title = Column(String)

    creator = Column(String)

    description = Column(Text)

    hashtags = Column(Text)

    thumbnail_url = Column(String)

    followers = Column(Integer)

    views = Column(Integer)

    likes = Column(Integer)

    comments = Column(Integer)

    engagement_rate = Column(Float)

    duration = Column(String)

    upload_date = Column(DateTime)