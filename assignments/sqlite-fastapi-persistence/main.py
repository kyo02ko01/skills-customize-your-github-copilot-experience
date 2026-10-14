import sqlite3
from contextlib import contextmanager

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Persistent Task API")
DATABASE_PATH = "tasks.db"


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)


class TaskUpdate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    completed: bool


class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool


@contextmanager
def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
    finally:
        connection.close()


def row_to_task(row: sqlite3.Row) -> TaskResponse:
    return TaskResponse(
        id=row["id"],
        title=row["title"],
        completed=bool(row["completed"]),
    )


@app.on_event("startup")
def initialize_database():
    # TODO: Create the tasks table if it does not exist.
    pass


@app.get("/tasks", response_model=list[TaskResponse])
def list_tasks():
    # TODO: Read every task from the database.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented")


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    # TODO: Read one task or raise a 404 error.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented")


@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    # TODO: Insert a task and return the saved row.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented")


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate):
    # TODO: Update a task or raise a 404 error.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented")


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    # TODO: Delete a task or raise a 404 error.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented")
