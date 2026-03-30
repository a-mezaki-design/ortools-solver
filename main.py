
from fastapi import FastAPI, Header
from pydantic import BaseModel
from typing import List

app = FastAPI()

# 合言葉（GAS側と合わせる）
SECRET_KEY = "my_password_123"

@app.post("/optimize")
async def solve(tasks: List[dict], x_api_key: str = Header(None)):
    if x_api_key != SECRET_KEY:
        return {"error": "合言葉が違います"}

    results = []
    for task in tasks:
        results.append({
            "id": task.get("id"),
            "start_time": "09:00", 
            "assigned": True
        })
    return {"results": results}
