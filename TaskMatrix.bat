@echo off
cd /d C:\Users\Danish\OneDrive\Desktop\TaskMatrix
call venv\Scripts\activate
start cmd /k "uvicorn backend.app.main:app --reload"
timeout /t 5
start http://127.0.0.1:8000
