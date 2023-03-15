from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request

router = APIRouter(
    tags=["Pages"]
)

templates = Jinja2Templates(directory='src/templates')


@router.get('/home', name='home')
def get_homepage(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})