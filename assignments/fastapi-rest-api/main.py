from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)


class TaskUpdate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    completed: bool


class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool


tasks: dict[int, TaskResponse] = {
    1: TaskResponse(id=1, title="Read the API assignment", completed=False),
    2: TaskResponse(id=2, title="Try the interactive API docs", completed=False),
}


@app.get("/tasks", response_model=list[TaskResponse])
def list_tasks():
    # TODO: Return all tasks.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented")


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    # TODO: Return the requested task or raise a 404 error.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented")


@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    # TODO: Create a task with a unique ID and completed=False.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented")


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate):
    # TODO: Replace the task or raise a 404 error.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented")


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    # TODO: Delete the task or raise a 404 error.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented")
