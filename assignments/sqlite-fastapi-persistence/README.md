# 📘 Assignment: Persisting FastAPI Data with SQLite

## 🎯 Objective

Extend a FastAPI task API to store tasks in a SQLite database. Practice creating a database table, using SQL to manage records, and checking that data remains available after the server restarts.

## 📝 Tasks

### 🛠️ Create the SQLite Database

#### Description
Set up the provided API so it creates a SQLite database and a `tasks` table when the server starts.

#### Requirements
Completed program should:

- Use Python's built-in `sqlite3` module and the database file `tasks.db`.
- Create the `tasks` table if it does not already exist.
- Store each task's integer ID, title, and completion state.
- Generate task IDs automatically and default new tasks to incomplete.
- Keep the existing FastAPI request and response models.

Use these commands from the assignment folder:

```bash
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

Open the interactive API documentation at `http://127.0.0.1:8000/docs`.


### 🛠️ Connect the API Endpoints to SQLite

#### Description
Replace the in-memory task storage with SQL queries so each endpoint reads and writes records in the database.

#### Requirements
Completed program should:

- Return all saved tasks from `GET /tasks` and one saved task from `GET /tasks/{task_id}`.
- Insert a task using `POST /tasks`, with a unique ID and an incomplete status by default.
- Update a task using `PUT /tasks/{task_id}`.
- Delete a task using `DELETE /tasks/{task_id}`.
- Return HTTP `404 Not Found` when an update, delete, or single-task lookup uses an ID that does not exist.
- Preserve the API's existing response fields and status codes.


### 🛠️ Verify Data Persists After Restart

#### Description
Use the API to make changes, restart the server, and confirm the database retains those changes.

#### Requirements
Completed program should:

- Create a task and confirm it appears in `GET /tasks`.
- Stop and restart the server, then confirm the task is still present.
- Update and delete tasks, then confirm the results with the read endpoints.
- Close each database connection after its queries are complete.
- **Optional stretch:** Add a query parameter to `GET /tasks` that filters tasks by their completion state.
