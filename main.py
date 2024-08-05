from typing import Union
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
import json
import requests

app = FastAPI(debug=True)

class Item(BaseModel):
    model: str
    prompt: str

urls = ["http://localhost:11434/api/generate"]

headers = {
    "Content-Type": "application/json"
}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/chat/{llms_name}")
async def update_item(llms_name: str, item: Item):
    if llms_name == "llama3":
        url = urls[0]
        payload = {
            "model": "llama3",
            "prompt": item.prompt,
            "stream": True
        }
        
        def generate():
            with requests.post(url, headers=headers, json=payload, stream=True) as response:
                if response.status_code == 200:
                    for line in response.iter_lines():
                        if line:
                            yield line.decode('utf-8')
                else:
                    yield f"Error: {response.status_code} - {response.text}"
        
        return StreamingResponse(generate(), media_type="text/plain")
    
    return {"item_name": item.model, "llms_name": llms_name}
