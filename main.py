from flask import Flask, render_template, request, jsonify, Blueprint
from flask_socketio import SocketIO, emit, send
import config as config
from models import db, User, Sensor

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/data", methods=["POST"])
def handle_data():
    data = request.get_json()
    if data:
        print("Received data:", data)
        send_data(data)
        return jsonify({"status": "success", "message": "Data received"}), 200
    else:
        return jsonify({"status": "error", "message": "No data received"}), 400

@app.route("/create_sensor", methods=["POST", "GET"])
def create_sensor():
    pass

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

def send_data(data):
    while True:
        socketio.emit('update_data', data)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
    with app.app_context():
        db.create_all(app)