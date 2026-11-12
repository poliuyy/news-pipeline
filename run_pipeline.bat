@echo off
set PYTHONIOENCODING=utf-8
cd /d C:\projects\news-pipeline 
call venv\Scripts\activate.bat
python main.py >> data\pipeline.log 2>&1