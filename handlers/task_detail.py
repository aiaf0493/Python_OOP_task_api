from flask import Request
from handlers.base import BaseHandler

class TaskDetailHandler(BaseHandler):

    def handle(self, request: Request, id: int) -> tuple[dict, int]:
        if request.method == "GET":
            return self._get_one(id)
        if request.method == "PUT":
            return self._update(request, id)
        if request.method == "DELETE":
            return self._delete(id)
        return self._error("Method not allowed", 405)

    def _get_one(self, id: int) -> tuple[dict, int]:
        task = self._repo.get_by_id(id)
        if task is None:
            return self._error(f"Task {id} not found", 404)
        return task.to_dict(), 200

    def _update(self, request: Request, id: int) -> tuple[dict, int]:
        data = request.get_json()
        if not data:
            return self._error("Request body is required", 400)
        try:
            task = self._repo.update(id, data)
            if task is None:
                return self._error(f"Task {id} not found", 404)
            return task.to_dict(), 200
        except ValueError as e:
            return self._error(str(e), 400)

    def _delete(self, id: int) -> tuple[dict, int]:
        success = self._repo.delete(id)
        if not success:
            return self._error(f"Task {id} not found", 404)
        return {"message": f"Task {id} deleted"}, 200