from repository.database import Base
from sqlalchemy import Identity, DateTime, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

# id : pk
# title : str
# image : 이미지 경로 str
# description : str
# tags : str > python, fastapi
# 생성일
# 이벤트 등록자 : user_id 


class Event(Base):

    __tablename__ = "events"

    id: Mapped[int] = mapped_column(Identity(start=1, increment=1), primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    image: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    tags: Mapped[str] = mapped_column(String(100), nullable=False)
    location: Mapped[str] = mapped_column(String(100), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    event_uploader: 
    user_id: Mapped[int] = mapped_column(ForeignKey("event_users.user_id"), nullable=False)

    # User 객체 연결 
    user:Mapped["User"] = relationship(back_populates="events")