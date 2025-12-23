from base import Base
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column



class User(Base):
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
