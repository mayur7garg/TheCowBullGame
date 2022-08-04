from pathlib import Path
from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_PATH = Path(__file__).parent.resolve()
app = FastAPI(title = 'The Cow Bull Game')
app.mount("/static", StaticFiles(directory = f"{BASE_PATH}/static"), name = "static")
templates = Jinja2Templates(directory=f"{BASE_PATH}/templates")

#with open(f'{BASE_PATH}/templates')

@app.get("/", response_class = HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
