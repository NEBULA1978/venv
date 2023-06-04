from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app=FastAPI()

@app.get("/",response_class=HTMLResponse)
def root():
    return """
    <html>
        <head>
            <title>Web FastAPI</title>
        </head>
        <body>
            <h1>Hi I a, a html file</h1>
        </body>
    </html>

    """