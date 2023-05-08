from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# Mock database
database = ['Item_0']

# Create
@app.post("/items/")
def create_item(item: str):
    database.append(item)
    return {"item": item}

# Read
@app.get("/items/")
def read_items():
    return {"items": database}

# Update
@app.put("/items/{item_id}")
def update_item(item_id: int, item: str):
    database[item_id] = item
    return {"item": item}

# Delete
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    item = database[item_id]
    del database[item_id]
    return {"item": item}

# Home
@app.get("/home/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Welcome to my API!</title>
        </head>
        <body>
            <h1>Welcome to my API!</h1>
            <p>This is a test page.</p>
        </body>
    </html>
    """
