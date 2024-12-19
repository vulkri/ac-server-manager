from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey


from database import Base

# Server configuration entry
class ServerConfigs(Base):
    __tablename__ = "server_configs"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    enabled = Column(Boolean, default=False)
    preset = Column(String)
    track_name = Column(Integer, index=True)
    ai = Column(Boolean)
    status = Column(String)

class Cars(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    
class CarSkins():
    __tablename__ = "car_skins"