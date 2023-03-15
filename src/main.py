from fastapi import Request
from src.heavy.router import app
from src.pages.router import router as router_pages
from fastapi.responses import RedirectResponse

app.include_router(router_pages)


@app.get('/hello_world')
def hello_world():
    return 'Hello World'


@app.get('/')
def show_homepage(request: Request):
    return RedirectResponse(request.url_for("home"))

