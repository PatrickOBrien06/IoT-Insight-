from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit, send
import logging
import config

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template("index.html")

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

def send_data(data):
    import time
    while True:
        time.sleep(5)
        socketio.emit('update_data', data)

@app.route("/data", methods=["POST"])
def handle_data():
    data = request.get_json()
    if data:
        print("Received data:", data)
        send_data(data)
        return jsonify({"status": "success", "message": "Data received"}), 200
    else:
        return jsonify({"status": "error", "message": "No data received"}), 400

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
