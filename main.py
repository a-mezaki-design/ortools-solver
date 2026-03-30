from fastapi import FastAPI, Header
from pydantic import BaseModel
from typing import List

app = FastAPI()

# データの「箱」の形を定義
class OptimizeRequest(BaseModel):
    tasks: List[dict]

SECRET_KEY = "my_password_123"

@app.post("/optimize")
async def solve(req: OptimizeRequest, x_api_key: str = Header(None)):
    if x_api_key != SECRET_KEY:
        return {"error": "合言葉が違います"}

    # req.tasks で「箱の中身」を取り出す
    tasks = req.tasks
    
    results = []
    for task in tasks:
        results.append({
            "id": task.get("id"),
            "start_time": "09:00", 
            "assigned": True
        })
    return {"results": results}
