
from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a root endpoint (GET request)
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Define a dynamic endpoint
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

# Define a POST endpoint
@app.post("/create/")
def create_item(name: str):
    return {"name": name, "status": "Item created successfully"}
