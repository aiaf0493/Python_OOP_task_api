from flask import Request
from handlers.base import BaseHandler

class TaskListHandler(BaseHandler):

    def handle(self, request: Request) -> tuple[dict, int]:
        if request.method == "GET":
            return self._get_all()
        if request.method == "POST":
            return self._create(request)
        return self._error("Method not allowed", 405)

    def _get_all(self) -> tuple[dict, int]:
        tasks = self._repo.get_all()
        return {"tasks": [t.to_dict() for t in tasks], "count": len(tasks)}, 200

    def _create(self, request: Request) -> tuple[dict, int]:
        data = request.get_json()
        if not data or "title" not in data:
            return self._error("title is required", 400)
        try:
            task = self._repo.create(
                title=data["title"],
                description=data.get("description", "")
            )
            return task.to_dict(), 201
        except ValueError as e:
            return self._error(str(e), 400)