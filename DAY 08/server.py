from flask import Flask, request

server = Flask(__name__)

@server.route('/', methods=['GET'])
def homepage():
    return "This is a homepage"

@server.route('/temperature', methods=['POST'])
def create_temperature():
    temp = request.get_json().get('temp')
    loc = request.get_json().get('loc')

    print(f"temp = {temp}, loc = {loc}")

    return "temperature is received"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)