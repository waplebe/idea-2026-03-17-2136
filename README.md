# Simple Task Tracker API

**Description:**

This project provides a simple RESTful API for managing tasks. It allows users to create, read, update, and delete tasks. A basic frontend is included for interacting with the API.

**Why it's useful:**

This is a practical example of a full-stack web service. It demonstrates a basic CRUD (Create, Read, Update, Delete) operation, which is a fundamental concept in web development. It's useful for learning about API design, backend development, and frontend interaction.

**Installation & Setup:**

1.  **Clone the repository:**
    ```bash
    git clone https://github/your-username/simple-task-tracker.git
    cd simple-task-tracker
    ```

2.  **Set up the backend:**
    *   Create a `.env` file in the root directory and populate it with the following (replace with your actual values):
        ```
        DATABASE_URL=sqlite:///tasks.db
        ```
    *   Run the backend server:
        ```bash
        python app.py
        ```

3.  **Set up the frontend:**
    *   Run the frontend development server:
        ```bash
        npm start
        ```

4.  **Access the frontend:**
    *   Open your web browser and navigate to `http://localhost:5000`.

**API Endpoints:**

*   `GET /tasks`: Retrieves all tasks.
*   `GET /tasks/{id}`: Retrieves a specific task by ID.
*   `POST /tasks`: Creates a new task.  Request body should be a JSON object with `title` and `description` fields.
*   `PUT /tasks/{id}`: Updates an existing task. Request body should be a JSON object with `title` and/or `description` fields.
*   `DELETE /tasks/{id}`: Deletes a task by ID.
*   `GET /health`:  Performs a health check of the API. Returns 200 OK if the API is running.

**Example Usage:**

*   **Create a task:**
    `POST /tasks`
    Request Body:
    ```json
    {
      "title": "Grocery Shopping",
      "description": "Buy milk, eggs, and bread"
    }
    ```
    Response:
    ```json
    {
      "id": 1,
      "title": "Grocery Shopping",
      "description": "Buy milk, eggs, and bread",
      "created_at": "2023-10-27T10:00:00Z"
    }
    ```

*   **Get all tasks:**
    `GET /tasks`
    Response:
    ```json
    [
      {
        "id": 1,
        "title": "Grocery Shopping",
        "description": "Buy milk, eggs, and bread",
        "created_at": "2023-10-27T10:00:00Z"
      }
    ]
    ```

**Dependencies:**

*   Python 3.7+
*   Flask
*   requests (for frontend testing)
*   sqlite3

**.gitignore:**

```
node_modules/
__pycache__/
.env
.env.example
*.pyc
*.log
```

**License:**

MIT License