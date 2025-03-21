from fastapi import FastAPI,APIRouter,Request
from postgres.db import connect_bd
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


router=APIRouter()



router.mount("/static",StaticFiles(directory="static"), name="static")
templates=Jinja2Templates(directory="templates")


@router.get("/",response_class=HTMLResponse)
async def get_books(request: Request):
    bd=connect_bd()
    bd.execute('select * from books')
    book=bd.fetchall()
    return templates.TemplateResponse('index.html', {"request": request, "message": book})
    
@router.get("/author",response_class=HTMLResponse)
def get_author(request: Request):
    bd=connect_bd()
    bd.execute('select author from books')
    author=bd.fetchall()
    return templates.TemplateResponse('author.html', {"request": request, "message": author})

@router.get("/name_book",response_class=HTMLResponse)
def get_name_book(request: Request):
    bd=connect_bd()
    bd.execute('select name_book from books')
    name_book=bd.fetchall()
    return templates.TemplateResponse('name.html', {"request": request, "message": name_book})


