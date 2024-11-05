from controller.task_controller import TaskController
from flask import Flask
from Task import db


def init_flask():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    return app


def init_db(app):
    with app.app_context():
        db.create_all()


app = init_flask()
task_controller = TaskController(app, db)

if __name__ == "__main__":
    init_db(app)
    app.run(debug=True)
