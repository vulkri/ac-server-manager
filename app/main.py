import os
import uuid
import datetime
from typing import Any
from urllib.parse import unquote

import starlette.status as status
from sqlalchemy.orm import Session

from fastapi import Body, Depends, FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from database import engine, SessionLocal
import models



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
def add_server(entry_data: dict, db: Session) -> models.ServerConfigEntry:

    server_config = models.ServerConfigEntry
    server_config = db.add(server_config(**entry_data))
    db.commit()
    
    return server_config

# Get server list from database
def get_serverlist(db: Session) -> dict:
    servers = db.query(models.ServerConfigEntry).order_by(models.ServerConfigEntry.id.desc()).all()
    servers_dict = [{column.name: getattr(row, column.name) for column in models.ServerConfigEntry.__table__.columns} for row in servers]
    
    return servers_dict


# Server list
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, db: Session=Depends(get_db)):
    serverlist = get_serverlist(db)

    context = {"serverlist": serverlist}

    return templates.TemplateResponse(
        request=request, name="serverlist.html", context=context
    )