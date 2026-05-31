from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import Float
from sqlalchemy import ForeignKey

from app.db.base import Base


class TranscriptChunk(Base):

    __tablename__ = "transcript_chunks"

    id = Column(Integer, primary_key=True)

    video_id = Column(
        Integer,
        ForeignKey("videos.id")
    )

    chunk_index = Column(Integer)

    chunk_text = Column(Text)

    source = Column(String)

    start_time = Column(Float)

    end_time = Column(Float)

    timestamp = Column(String)