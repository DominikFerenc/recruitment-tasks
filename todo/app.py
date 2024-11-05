from config.config import Config
from controller.task_controller import TaskController
from flask import Flask
from models.task import db


def init_flask():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    return app


def init_db(app):
    with app.app_context():
        db.create_all()


app = init_flask()

if __name__ == "__main__":
    init_db(app)
    task_controller = TaskController(app, db)
    app.run(debug=True)
