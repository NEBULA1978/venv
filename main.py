from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

app=FastAPI()

app.mount("/static",StaticFiles(directory="./public/static"),name="static")

# Ruta para archivos html
@app.get("/",response_class=HTMLResponse)
def root():
    html_address = "./public/static/index.html"
    return FileResponse(html_address,status_code=200)