# todo_app_in_memory.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app instance
app = FastAPI()

# Define CORS policy to allow requests from anywhere (wildcard '*')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)

# In-memory list to store todo items
todos = []

class TodoItem(BaseModel):
    title: str
    description: str

@app.get("/todos", response_model=List[TodoItem])
async def get_todos():
    return todos

@app.post("/todos", response_model=TodoItem)
async def create_todo(todo: TodoItem):
    todos.append(todo)
    return todo

@app.delete("/todos/{todo_index}", status_code=204)
async def delete_todo(todo_index: int):
    try:
        todos.pop(todo_index)
        return {"message": "Todo deleted successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Todo not found")
