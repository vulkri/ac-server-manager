from typing import List
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

# Server configuration
class ServerConfig(Base):
    __tablename__ = "server_config"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    enabled: Mapped[bool] = mapped_column(default=False)
    preset: Mapped[str] = mapped_column(String(30))
    
    ai: Mapped[bool] = mapped_column(default=False)
    status: Mapped[str] = mapped_column(String(10))

# Car - parent of car_skin
class Car(Base):
    __tablename__ = "car"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(50))
    name: Mapped[str] = mapped_column(String(250))
    data_path: Mapped[str] = mapped_column(String(100))
    skins: Mapped[List["CarSkin"]] = relationship(back_populates="car")
    
# Car's skins - chilren of the Car
class CarSkin(Base):
    __tablename__ = "car_skin"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(50))
    preview_path: Mapped[str] = mapped_column(String(100))
    car_id: Mapped[int] = mapped_column(ForeignKey("car.id"))
    car: Mapped["Car"] = relationship(back_populates="skins")