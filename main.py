from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse

app=FastAPI()

# Ruta para archivos html
@app.get("/",response_class=HTMLResponse)
def root():
    html_address = "./public/html/index.html"
    return FileResponse(html_address,status_code=200)