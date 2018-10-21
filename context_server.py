import flask
from flask import request
from multiprocessing.connection import Client
import Queue
import thread
import socket

HOST = '127.0.0.1'
PORT = 10004


sendSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sendSocket.connect((HOST, PORT))

app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/context', methods = ['POST'])
def get_context():  
	data = request.get_json() # a multidict containing POST data
	print data
	sendSocket.sendall(data["closest"].encode())
	return '200'

if __name__=='__main__':
    app.run(host='10.128.3.108', port=3131)


