from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app=FastAPI()

app.mount("/static",StaticFiles(directory="./public/static"),name="static")

templates = Jinja2Templates(directory="./public/templates")

# Ruta para archivos html
@app.get("/",response_class=HTMLResponse)
def root():
    html_address = "./public/static/index.html"
    return FileResponse(html_address,status_code=200)

# Ruta para Jinja2
@app.get("/template/{id}", response_class=HTMLResponse)
def template(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})
