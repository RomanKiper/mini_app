from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

app = FastAPI()

# Mount static and templates
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

@app.get("/mini_app", response_class=HTMLResponse)
async def mini_app(request: Request):
    return templates.TemplateResponse("mini_app.html", {"request": request})
