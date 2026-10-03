from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Basis AI Furniture API")

class FurnitureRequest(BaseModel):
    prompt: str

@app.post("/api/generate")
def generate_furniture(req: FurnitureRequest):
    user_text = req.prompt.lower()
    
    # Базовые размеры по умолчанию
    width, height, depth = 1200, 2400, 600
    
    if "тумба" in user_text:
        width, height, depth = 600, 800, 500
    elif "кухня" in user_text:
        width, height, depth = 2400, 850, 600

    # Возвращаем параметры, которые подхватит скрипт Базиса
    return {
        "status": "success",
        "description": f"Запрос обработан: {req.prompt}",
        "dimensions": {
            "width": width,
            "height": height,
            "depth": depth,
            "material_thickness": 16
        }
    }