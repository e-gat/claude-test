from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello Universe</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: sans-serif;
            }
            h1 { font-size: 3rem; }
        </style>
    </head>
    <body>
        <h1>Hello Universe</h1>
    </body>
    </html>
    """
