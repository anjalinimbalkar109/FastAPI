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
    title = Column(String, nullable=False)
    completed = Column(Boolean, default=False, nullable=False)


class TodoCreate(BaseModel):
    title: str
    completed: bool = False


class TodoUpdate(BaseModel):
    title: str
    completed: bool = False


Base.metadata.create_all(bind=engine)


def serialize_todo(todo: Todo):
    return {"id": todo.id, "title": todo.title, "completed": bool(todo.completed)}


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/todos", status_code=status.HTTP_201_CREATED)
def create_todo(
    todo_data: TodoCreate | None = None,
    title: str | None = None,
    completed: bool = False,
    db: Session = Depends(get_db),
):
    if todo_data is not None:
        todo = Todo(title=todo_data.title, completed=todo_data.completed)
    else:
        if not title:
            raise HTTPException(status_code=400, detail="Title is required")
        todo = Todo(title=title, completed=completed)

    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {"message": "Todo created", "data": serialize_todo(todo)}


@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return {"total": len(todos), "data": [serialize_todo(todo) for todo in todos]}


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return serialize_todo(todo)

# Update
@app.put("/todos/{todos_id}")
def update_todo(todo_id:int, title:str, db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404,detail="Todo not found")
    todo.title = title

    db.commit()
    db.refresh(todo)
    
    return {
        "message" : "Todo updated.",
        "data" : todo
    }

  

