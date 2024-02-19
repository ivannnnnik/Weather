from app import create_db


def on_starting(server):
    create_db()


bind = "0.0.0.0:5000"
workers = 4
