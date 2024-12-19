import os
import uuid
import datetime
from typing import Any
from urllib.parse import unquote
import threading

import starlette.status as status
from sqlalchemy.orm import Session

from fastapi import Body, Depends, FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from database import engine, SessionLocal
import models
from server_management import background_monitor, start_server



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

models.Base.metadata.create_all(bind=engine)

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Add new server config
def add_server(server_data: dict, db: Session) -> models.ServerConfigs:

    server_config = models.ServerConfigs
    server_config = db.add(server_config(**server_data))
    db.commit()
    
    return server_config

# Get server list from database
def get_serverlist(db: Session) -> dict:
    servers = db.query(models.ServerConfigs).order_by(models.ServerConfigs.id.desc()).all()
    servers_dict = [{column.name: getattr(row, column.name) for column in models.ServerConfigs.__table__.columns} for row in servers]

    return servers_dict


# Server list
@app.get("/", response_class=HTMLResponse)
def get_server_list(request: Request, db: Session=Depends(get_db)):
    serverlist = get_serverlist(db)

    context = {"serverlist": serverlist}

    return templates.TemplateResponse(
        request=request, name="serverlist.html", context=context
    )


# Car list
@app.get("/cars/", response_class=HTMLResponse)
def get_car_list(request: Request, db: Session=Depends(get_db)):
    carlist = []

    context = {"carlist": carlist}

    return templates.TemplateResponse(
        request=request, name="serverlist.html", context=context
    )

# Add car

# Delete car

# Rate car 

# Start test server
start_server("test", 1, "test.txt")

# Start background monitor
monitor_thread = threading.Thread(target=background_monitor, daemon=True)
monitor_thread.start()