from flask import Flask, render_template, request, jsonify, Blueprint, flash
from flask_socketio import SocketIO, emit, send
import config as config
from models import db, User, Sensor, SensorData

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
socketio = SocketIO(app)
db.init_app(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/create_sensor", methods=["POST", "GET"])
def create_sensor():
    if request.method == "POST":
        sensor_id = request.form.get("sensor_id")
        sensor_name = request.form.get("sensor_name")

        sensor_exists = Sensor.query.filter_by(sensor_id=sensor_id).first()

        if not sensor_exists:
            sensor = Sensor(sensor_id=sensor_id, sensor_name=sensor_name)
            db.session.add(sensor)
            db.session.commit()
            flash("Added sensor!", "success")
            print("Added sensor")
        
        else:
            flash("Sensor already exists!", "error")
            print("Sensor already exists!")

    return render_template("create_sensor.html")


@app.route("/data", methods=["POST"])
def handle_data():
    data = request.get_json() 
    data_exists = Sensor.query.filter_by(sensor_id=data["id"]).first()
    if data and data_exists:
        print("Received data:", data)
        print(data["data"])
        send_data(data)
        return jsonify({"status": "success", "message": "data received"}), 200
    else:
        return jsonify({"status": "error", "message": "No data received"}), 400
    


@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

def send_data(data):
    while True:
        socketio.emit('update_data', data)

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
    