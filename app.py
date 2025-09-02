from flask import Flask, render_template,request
from flask_socketio import SocketIO,emit
import random

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
        return render_template('index.html')

# to listen connect event
@socketio.on("connect")
def handle_connect():
        username = f"User_{random.randint(1000,9999)}"
        gender = random.choice(["girl","boy"])

if __name__ == "__main__":
        socketio.run(app)
