from datetime import timedelta

from fastapi import FastAPI, APIRouter, Depends, Request, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

# from routers import photo
from routers import user

# from db import models

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_homepage(request: Request):
    return templates.TemplateResponse("index.html", { "request": request })


# /api router
api = APIRouter()
app.include_router(user.router)
# api.include_router(photo.router, prefix="/photos")
app.include_router(api, prefix="/api/v1")
