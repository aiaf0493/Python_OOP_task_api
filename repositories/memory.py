from typing import List, Optional
from models.task import Task
from repositories.base import TaskRepository

class InMemoryRepository(TaskRepository):

    def __init__(self):
        self._store: dict[int, Task] = {}
        self._next_id: int = 1

    def get_all(self) -> List[Task]:
        return list(self._store.values())

    def get_by_id(self, id: int) -> Optional[Task]:
        return self._store.get(id)

    def create(self, title: str, description: str = "") -> Task:
        task = Task(self._next_id, title, description)
        self._store[self._next_id] = task
        self._next_id += 1
        return task

    def update(self, id: int, data: dict) -> Optional[Task]:
        task = self._store.get(id)
        if task is None:
            return None
        if "title" in data:
            task.title = data["title"]
        if "description" in data:
            task.description = data["description"]
        if "status" in data:
            task.status = data["status"]
        return task

    def delete(self, id: int) -> bool:
        if id not in self._store:
            return False
        del self._store[id]
        return True