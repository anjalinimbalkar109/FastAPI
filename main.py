from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI()

todos = []

class Todo(BaseModel):
    id : int
    title: str
    completed: bool

# Create a new todo
@app.post("/todos")
def post_todos(todo : Todo):
    todos.append(todo)
    return{
    "message": "Todo created successfully",
    }

# Read all todos
@app.get("/todos")
def get_todos():
    return {
        "todos": todos
    }

# Read a specific todo by ID
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"error": "Todo not found"}

# Update 
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,updated_todo:Todo):    
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {
                "message": "Todo updated successfully",
                "data": updated_todo
            }      
    return {"error" : "Todo not found"}   

#Delete 
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for index,todo in enumerate(todos):
        if todo.id == todo_id: 
            todos.pop(index)
            return{ "message": "Todo deleted successfully"}
    return {"error" : "Todo not found"}        