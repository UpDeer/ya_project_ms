from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
import pandas as pd
import tempfile
import os

app = FastAPI(title="CSV Reader")

# Настраиваем шаблоны
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    # Проверяем расширение файла
    if not file.filename.endswith('.csv'):
        return {"error": "Файл должен быть в формате CSV"}
    
    try:
        # Читаем содержимое файла
        content = await file.read()
        
        # Создаем временный файл
        with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as temp_file:
            temp_file.write(content)
            temp_file_path = temp_file.name
        
        # Читаем CSV файл с помощью pandas
        df = pd.read_csv(temp_file_path)
        
        # Удаляем временный файл
        os.unlink(temp_file_path)
        
        # Преобразуем DataFrame в словарь
        data = df.to_dict(orient="records")
        
        return {"data": data}
    
    except Exception as e:
        return {"error": f"Ошибка при обработке файла: {str(e)}"} 