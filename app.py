from flask import Flask, jsonify, request
from repositories.memory import InMemoryRepository
from handlers.task_list import TaskListHandler
from handlers.task_detail import TaskDetailHandler

app = Flask(__name__)

repo = InMemoryRepository()
list_handler = TaskListHandler(repo)
detail_handler = TaskDetailHandler(repo)

@app.route("/tasks", methods=["GET", "POST"])
def task_list():
    body, status = list_handler.handle(request)
    return jsonify(body), status

@app.route("/tasks/<int:id>", methods=["GET", "PUT", "DELETE"])
def task_detail(id: int):
    body, status = detail_handler.handle(request, id)
    return jsonify(body), status

if __name__ == "__main__":
    app.run(debug=True)