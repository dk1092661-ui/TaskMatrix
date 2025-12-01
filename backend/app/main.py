from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# STATIC & TEMPLATE SETUP (FINAL FIX)
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "static")),
    name="static",
)

templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


# ---------- LOGIN ----------
@app.get("/", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
def do_login(username: str = Form(...), password: str = Form(...)):
    # (Dummy login for now)
    return RedirectResponse("/todo", status_code=303)


# ---------- TODO ----------
@app.get("/todo", response_class=HTMLResponse)
def todo(request: Request):
    return templates.TemplateResponse("todo.html", {"request": request})


@app.get("/completed", response_class=HTMLResponse)
def completed(request: Request):
    return templates.TemplateResponse("completed.html", {"request": request})


@app.get("/logout")
def logout():
    return RedirectResponse("/", status_code=302)


# ---------- SIGNUP ----------
@app.get("/signup", response_class=HTMLResponse)
def signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@app.post("/signup")
def do_signup():
    return RedirectResponse("/", status_code=303)


# ---------- FORGOT PASSWORD ----------
@app.get("/forgot", response_class=HTMLResponse)
def forgot(request: Request):
    return templates.TemplateResponse("forgot.html", {"request": request})

@app.post("/forgot")
def do_forgot():
    return RedirectResponse("/", status_code=303)
