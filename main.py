from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import logging
import config


app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
socketio = SocketIO(app)

@app.route('/')
def index():
    return 'WebSocket Server'

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(data):
    print('Received message: ' + data)
    emit('response', {'data': 'Message received'})


@app.route("/data", methods=["POST"])
def handle_data():
    data = request.get_json()
    if data:
        print("Received data:", data)
        return jsonify({"status": "success", "message": "Data received"}), 200
    else:
        return jsonify({"status": "error", "message": "No data received"}), 400

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
