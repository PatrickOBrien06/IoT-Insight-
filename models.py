from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)


class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)