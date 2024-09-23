from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import sys
import os

# Import my package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'rubik')))

from rubik.RubikChecker import RubikChecker
from rubik.Rubik import Rubik

class RubikModel(BaseModel):
    content: List[List[List[str]]]

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

@app.post("/check_cube", status_code=status.HTTP_200_OK)
async def check_cube(body: RubikModel):
    if (body.content is None):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The provided rubik is invalid. Please check the format and try again.")

    try:
        rubik = Rubik(body.content)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The server is unable to initialize the rubik. Please check the format and try again.")

    try:
        if rubik.isSolvable() == False:
            raise Exception
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The provided rubik is impossible to solve. Please check all faces and try again.")
    return {
        "response": 200,
        "solvable": True
    }

# curl -s -H 'Content-Type: application/json' -d '{ "name":"foo"}' -X POST http://127.0.0.1:8000/test/ | jq

if __name__ == "__main__":
    from rubik.main import basic_function
    import time
    basic_function();
    for i in range(1200):
        print(f"Time : {i}")
        time.sleep(1);

