# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API for managing tasks with FastAPI. Practice defining request and response models, handling HTTP methods, validating input, and returning appropriate status codes.

## 📝 Tasks

### 🛠️ Define the API and Task Models

#### Description
Set up the provided starter code, run the FastAPI server, and inspect the interactive API documentation before implementing the endpoints.

#### Requirements
Completed program should:

- Install the packages listed in `requirements.txt` and start the application with Uvicorn.
- Open the interactive API documentation at `http://127.0.0.1:8000/docs`.
- Define a task response model with an integer `id`, a string `title`, and a boolean `completed` field.
- Define request models for creating and updating tasks.
- Require task titles to contain between 1 and 100 characters.

Use these commands from the assignment folder:

```bash
python -m pip install -r requirements.txt
uvicorn main:app --reload
```


### 🛠️ Implement the Read Endpoints

#### Description
Add endpoints that let clients retrieve every task or retrieve one task by its ID.

#### Requirements
Completed program should:

- Return all tasks from `GET /tasks` as a JSON array.
- Return the matching task from `GET /tasks/{task_id}`.
- Return HTTP `404 Not Found` when the requested task ID does not exist.
- Return task objects with `id`, `title`, and `completed` fields.


### 🛠️ Implement the Create, Update, and Delete Endpoints

#### Description
Add endpoints that let clients create a task, replace an existing task, and delete a task.

#### Requirements
Completed program should:

- Create a task from a JSON request body sent to `POST /tasks` and return HTTP `201 Created`.
- Assign each new task a unique integer ID and set `completed` to `false` when creating it.
- Replace a task's title and completion state with `PUT /tasks/{task_id}`.
- Return HTTP `404 Not Found` when an update or delete targets a task ID that does not exist.
- Delete a task with `DELETE /tasks/{task_id}` and return HTTP `204 No Content` when successful.
- Let FastAPI return HTTP `422 Unprocessable Entity` for request data that fails model validation.
