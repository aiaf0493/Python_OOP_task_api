from abc import ABC, abstractmethod
from flask import Request, Response
from repositories.base import TaskRepository

class BaseHandler(ABC):

    def __init__(self, repo: TaskRepository):
        self._repo = repo

    @abstractmethod
    def handle(self, request: Request) -> tuple[dict, int]:
        pass

    def _error(self, message: str, code: int) -> tuple[dict, int]:
        return {"error": message}, code