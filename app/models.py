from sqlalchemy import Column, DateTime, Integer, String, Boolean


from database import Base

# Server configuration entry
class ServerConfigEntry(Base):
    __tablename__ = "server_config"

    id = Column(Integer, primary_key=True)
    server_name = Column(String, index=True)
    preset = Column(String)
    track_name = Column(Integer, index=True)
    ai = Column(Boolean)
    status = Column(String)
