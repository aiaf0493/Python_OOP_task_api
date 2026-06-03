from datetime import datetime
from typing import Optional

class Task:
    VALID_STATUSES = {"pending", "in_progress", "done"}

    def __init__(self, id: int, title: str, description: str = "", status: str = "pending"):
        self._id = id
        self._title = title
        self._description = description
        self._status = status
        self._created_at = datetime.utcnow()
        self._updated_at = datetime.utcnow()

    @property
    def id(self) -> int:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        if not value or not value.strip():
            raise ValueError("Title cannot be empty")
        self._title = value.strip()
        self._updated_at = datetime.utcnow()

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = value
        self._updated_at = datetime.utcnow()

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str):
        if value not in self.VALID_STATUSES:
            raise ValueError(f"Invalid status: '{value}'. Must be one of {self.VALID_STATUSES}")
        self._status = value
        self._updated_at = datetime.utcnow()

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "title": self._title,
            "description": self._description,
            "status": self._status,
            "created_at": self._created_at.isoformat(),
            "updated_at": self._updated_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        task = cls(
            id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            status=data.get("status", "pending"),
        )
        if "created_at" in data:
            task._created_at = datetime.fromisoformat(data["created_at"])
        if "updated_at" in data:
            task._updated_at = datetime.fromisoformat(data["updated_at"])
        return task

    def __repr__(self) -> str:
        return f"Task(id={self._id}, title='{self._title}', status='{self._status}')"