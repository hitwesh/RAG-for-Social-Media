from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.db.base import Base


class Conversation(Base):

    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True)

    session_id = Column(String)