import flask
from flask import request
import serial
ser=serial.Serial('/dev/ttyACM0')

app = flask.Flask(__name__)
state = 1
@app.route("/")
def hello():
    return "Hello World!"

@app.route('/servo', methods = ['POST'])
def get_context():
        data = request.get_json() # a multidict containing POST data
        print data
        if data["servo"] == 1:
            print "clk"
            if state == 1:
                ser.write(b'1')
                state = 2
            else:
                ser.write(b'2')
                state = 1

        else:
            print "cclk"
            ser.write(b'2')
        return '200'


if __name__=='__main__':
    app.run(host='10.128.13.41', port=3139)
