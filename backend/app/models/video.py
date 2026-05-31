from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime

from app.db.base import Base


class Video(Base):

    __tablename__ = "videos"

    id = Column(Integer, primary_key=True)

    platform = Column(String)

    url = Column(String)

    creator = Column(String)

    followers = Column(Integer)

    views = Column(Integer)

    likes = Column(Integer)

    comments = Column(Integer)

    engagement_rate = Column(Float)

    duration = Column(String)

    upload_date = Column(DateTime)