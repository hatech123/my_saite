from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app=FastAPI()

@app.get("/")
def read_root():
    html_content="""
    <h2>Mega Robot</h2>
    <form action="/about">
        <button>About us </button>
    </form>
    <h3>Information</h3>
    <h3>Information</h3>
    <h3>Information</h3>
    <h3>Information</h3>
    <form>
        <label>Login___</ladel>
        <input type="text">
    </form>
        <form>
        <label>Password</ladel>
        <input type="text">
    </form>
    <button>Send </button>
    """


    return HTMLResponse(content=html_content)

@app.get("/about")
def read_about():
    html_content="""
    <h2>address: Astrakhan</h2>
    <form action="/">
        <button>Start page </button>
    </form>
    """
    return HTMLResponse(content=html_content)