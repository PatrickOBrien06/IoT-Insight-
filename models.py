from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)


class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.Integer, nullable=False, unique=True)
    sensor_name = db.Column(db.Integer, nullable=False)


class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reading = db.Column(db.Float, nullable=False)