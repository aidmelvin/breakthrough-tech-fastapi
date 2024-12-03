
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Setting up FastAPI and SQLAlchemy
app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"  # SQLite database file

# SQLAlchemy ORM setup
Base = declarative_base()
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Defining Todo model
class TodoItem(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Pydantic schema for Todo item
class TodoCreate(BaseModel):
    title: str
    description: str

class TodoResponse(TodoCreate):
    id: int

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/todos", response_model=List[TodoResponse])
async def get_todos(db: Session = next(get_db())):
    return db.query(TodoItem).all()

@app.post("/todos", response_model=TodoResponse)
async def create_todo(todo: TodoCreate, db: Session = next(get_db())):
    db_todo = TodoItem(title=todo.title, description=todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.delete("/todos/{todo_id}", status_code=204)
async def delete_todo(todo_id: int, db: Session = next(get_db())):
    db_todo = db.query(TodoItem).filter(TodoItem.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return {"message": "Todo deleted successfully"}
