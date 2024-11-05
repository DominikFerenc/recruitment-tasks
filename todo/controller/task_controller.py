from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models.task import Task


class TaskController:
    def __init__(self, app, db):
        self.app = app
        self.db = db
        self.init_routes()

    def init_routes(self):
        @self.app.route("/tasks", methods=["GET"])
        def get_tasks():
            tasks = Task.query.all()
            return jsonify([task.to_dict() for task in tasks])

        @self.app.route("/tasks", methods=["POST"])
        def create_task():
            data = request.get_json()
            new_task = Task(title=data["title"])
            self.db.session.add(new_task)
            self.db.session.commit()
            return jsonify(new_task.to_dict()), 201

        @self.app.route("/tasks/<int:task_id>", methods=["GET"])
        def get_task(task_id):
            task = Task.query.get_or_404(task_id)
            return jsonify(task.to_dict())

        @self.app.route("/tasks/<int:task_id>", methods=["PUT"])
        def update_task(task_id):
            task = Task.query.get_or_404(task_id)
            data = request.get_json()
            task.title = data["title"]
            task.completed = data.get("completed", task.completed)
            self.db.session.commit()
            return jsonify(task.to_dict())

        @self.app.route("/tasks/<int:task_id>", methods=["DELETE"])
        def delete_task(task_id):
            task = Task.query.get_or_404(task_id)
            self.db.session.delete(task)
            self.db.session.commit()
            return jsonify({"message": "Task deleted successfully"}), 204
