from repository.database import Base
from sqlalchemy import Identity, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

# user_id : pk
# email : unique
# password
# name
# 가입일


class User(Base):

    __tablename__ = "event_users"

    user_id: Mapped[int] = mapped_column(
        Identity(start=1, increment=1), primary_key=True
    )
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    #  Event 객체 연결
    events : Mapped[list["Event"]] = relationship(back_populates="user")