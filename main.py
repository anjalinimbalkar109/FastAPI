from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(String)


# class TodoCreate(BaseModel):
#     title: str
#     completed: bool = False


# class TodoUpdate(BaseModel):
#     title: str
#     completed: bool = False


Base.metadata.create_all(bind=engine)


# def serialize_todo(todo: Todo):
#     return {"id": todo.id, "title": todo.title, "completed": bool(todo.completed)}


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/todos", status_code=status.HTTP_201_CREATED)
def create_todo(title: str, db: Session = Depends(get_db),):
    todo = Todo(title = title ,completed=False)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {"message": "Todo created", "data":todo}


@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return { "data": todos }


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

# Delete
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int,db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {
        "message" : "Todo deleted"
    }
  

