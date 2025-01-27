# fastapi_celery
Example of FastAPI with Celery

Use Docker to start the application:
```bash
docker-compose up --build
```

## Endpoints

### `POST /new_schedule`
This endpoint creates a new task based on the provided parameters.

#### **Response:**
- Returns the unique identifier of the task (`task_id`):
```json
{
    "task_id": "a36ff235-af1a-..."
}
```

---

### `GET /schedule_status/{task_id}`
This endpoint returns the **status** of a submitted task.

#### **URL Parameter:**
- **`task_id`**: The unique identifier of the task.

#### **Possible Status:**
- **`PENDING`**: Waiting for execution or unknown `task_id`.
- **`STARTED`**: The task has started.
- **`SUCCESS`**: The task has been successfully completed.
- **`FAILURE`**: The task failed due to an error.
- **`RETRY`**: The task is being retried after a temporary failure.
- **`REVOKED`**: The task has been canceled.

#### **Example Response:**
```json
"Status of the Task STARTED"
```

---

### `GET /schedule_result/{task_id}`
This endpoint returns the **results** of a task based on the `task_id`.

#### **URL Parameter:**
- **`task_id`**: The unique identifier of the task.

#### **Example Response:**
```json
"Result of the Task: 42"
```
