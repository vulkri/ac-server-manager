from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

# Server configuration entry
class ServerConfigs(Base):
    __tablename__ = "server_configs"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    enabled: Mapped[bool] = mapped_column(default=False)
    preset: Mapped[str] = mapped_column(String(30))
    
    ai: Mapped[bool] = mapped_column(default=False)
    status: Mapped[str] = mapped_column(String(10))

class Cars(Base):
    __tablename__ = "cars"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    
class CarSkins():
    __tablename__ = "car_skins"