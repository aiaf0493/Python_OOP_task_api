# Python OOP Task API
 
A RESTful Task Management API built with Python and Flask,  
demonstrating four core Object-Oriented Programming principles.
 
---
 
## OOP Concepts Applied
 
| Concept | Where Applied |
|---------|--------------|
| Encapsulation | `Task` class — private fields + `@property` setters |
| Abstraction | `TaskRepository` ABC — storage interface |
| Inheritance | `BaseHandler` → `TaskListHandler`, `TaskDetailHandler` |
| Polymorphism | `handle()` method overridden per handler |
 
---
 
## Project Structure
 
    task_api/
    ├── app.py
    ├── models/
    │   └── task.py
    ├── repositories/
    │   ├── base.py
    │   ├── memory.py
    │   └── file.py
    └── handlers/
        ├── base.py
        ├── task_list.py
        └── task_detail.py
 
---
 
## How to Run
 
    conda activate task_api
    python app.py
 
Server runs at `http://localhost:5000`
 
---
 
## API Endpoints
 
| Method | Endpoint | Description | Status Code |
|--------|----------|-------------|-------------|
| GET | `/tasks` | List all tasks | 200 |
| POST | `/tasks` | Create a task | 201 |
| GET | `/tasks/<id>` | Get a single task | 200 |
| PUT | `/tasks/<id>` | Update a task | 200 |
| DELETE | `/tasks/<id>` | Delete a task | 200 |
 
---
 
## Example Usage
 
**Create a task:**
 
    Invoke-RestMethod -Uri http://localhost:5000/tasks `
      -Method POST `
      -ContentType "application/json" `
      -Body '{"title": "Study OOP", "description": "Review inheritance"}'
 
**Get all tasks:**
 
    Invoke-RestMethod -Uri http://localhost:5000/tasks -Method GET
 
**Update status:**
 
    Invoke-RestMethod -Uri http://localhost:5000/tasks/1 `
      -Method PUT `
      -ContentType "application/json" `
      -Body '{"status": "done"}'
 
Valid status values: `pending` · `in_progress` · `done`
 
---
 
## Storage Backends
 
Switching storage requires **one line change** in `app.py`:
 
    repo = InMemoryRepository()          # default (in-memory)
    repo = FileRepository("tasks.json")  # persistent (file)
 