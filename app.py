from flask import Flask, render_template

from flask_socketio import SocketIO, send, emit

from dotenv import load_dotenv

import os

chat = []

load_dotenv()

app = Flask(__name__,template_folder="templates")


app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
socketio = SocketIO(app)    

@app.route('/')
def index():
    return render_template("index.html")

@socketio.on('message')
def handelMensagge(msg):
    chat.append(msg)
    emit('chat',chat)


@socketio.on('delete')
def handelMensagge(msg):

    chat.remove(msg)

    emit('chat',chat)

if __name__ ==  '__main__':
    socketio.run(app= app, port=3000, debug= True, host= "0.0.0.0") 