import json
import os
from typing import List, Optional
from models.task import Task
from repositories.base import TaskRepository

class FileRepository(TaskRepository):

    def __init__(self, filepath: str = "tasks.json"):
        self._filepath = filepath
        if not os.path.exists(self._filepath):
            self._save([])

    def _load(self) -> List[Task]:
        with open(self._filepath, "r") as f:
            return [Task.from_dict(d) for d in json.load(f)]

    def _save(self, tasks: List[Task]):
        with open(self._filepath, "w") as f:
            json.dump([t.to_dict() for t in tasks], f, indent=2)

    def _next_id(self, tasks: List[Task]) -> int:
        return max((t.id for t in tasks), default=0) + 1

    def get_all(self) -> List[Task]:
        return self._load()

    def get_by_id(self, id: int) -> Optional[Task]:
        return next((t for t in self._load() if t.id == id), None)

    def create(self, title: str, description: str = "") -> Task:
        tasks = self._load()
        task = Task(self._next_id(tasks), title, description)
        tasks.append(task)
        self._save(tasks)
        return task

    def update(self, id: int, data: dict) -> Optional[Task]:
        tasks = self._load()
        target = next((t for t in tasks if t.id == id), None)
        if target is None:
            return None
        if "title" in data:
            target.title = data["title"]
        if "description" in data:
            target.description = data["description"]
        if "status" in data:
            target.status = data["status"]
        self._save(tasks)
        return target

    def delete(self, id: int) -> bool:
        tasks = self._load()
        new_tasks = [t for t in tasks if t.id != id]
        if len(new_tasks) == len(tasks):
            return False
        self._save(new_tasks)
        return True