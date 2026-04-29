# import fastpi
from fastapi import FastAPI

import os
import uvicorn



app = FastAPI()


# create a simple calculator API

@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}       

@app.get("/subtract")
def subtract(a: float, b: float):    
    return {"result": a - b}



if __name__ == "__main__":
    # Get port from environment or default to 8000 for local testing
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
