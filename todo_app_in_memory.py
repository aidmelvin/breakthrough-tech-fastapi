# todo_app_in_memory.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory list to store todo items
todos = []

class TodoItem(BaseModel):
    title: str
    description: str

class TodoDeleteItemModel(BaseModel):
    id: int

@app.get("/todos")
async def get_todos():
    return todos

@app.post("/todos")
async def create_todo(todo: TodoItem):
    todos.append(todo)
    return todo

@app.delete("/todos")
async def delete_todo(todo_index: TodoDeleteItemModel):
    try:
        todos.pop(todo_index.id)
        return {"message": "Todo deleted successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Todo not found")

############# ALSO SHOW THIS:

# @app.delete("/todos/{todo_index}")
# async def delete_todo(todo_index: int):
#     try:
#         todos.pop(todo_index)
#         return {"message": "Todo deleted successfully"}
#     except IndexError:
#         raise HTTPException(status_code=404, detail="Todo not found")
