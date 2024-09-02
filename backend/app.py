from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# Import my package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'project_name')))


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class Test(BaseModel):
     name: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
	return {
		"response": 200,
		"message": "API is working !"
	}

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.post("/test")
async def test_post(test: Test):
     print(test)
     return {
          "response": 200,
          "message": test.name
	 }

# curl -s -H 'Content-Type: application/json' -d '{ "name":"foo"}' -X POST http://127.0.0.1:8000/test/ | jq

if __name__ == "__main__":
    from project_name.main import basic_function
    import time
    basic_function();
    for i in range(1200):
        print(f"Time : {i}")
        time.sleep(1);

