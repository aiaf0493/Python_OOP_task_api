from abc import ABC, abstractmethod
from typing import List, Optional
from models.task import Task

class TaskRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Task]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Task]:
        pass

    @abstractmethod
    def create(self, title: str, description: str = "") -> Task:
        pass

    @abstractmethod
    def update(self, id: int, data: dict) -> Optional[Task]:
        pass

    @abstractmethod
    def delete(self, id: int) -> bool:
        pass