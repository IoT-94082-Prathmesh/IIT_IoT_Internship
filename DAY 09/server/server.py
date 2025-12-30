from flask import Flask, render_template, request

server = Flask(__name__)

@server.route("/", methods=['GET'])
def homepage():
    return render_template("homepage.html")

@server.route('/welcome', methods=['GET'])
def welcome():
    return render_template("welcome.html", message="IoT Application")

@server.route('/temperatures', methods=['GET'])
def retrieve_temperatures():
    temps = [(27, "hall"), (26, "CT01"), (26, "CT02"), (27, "Library")]
    return render_template("table.html", message=temps)

@server.route('/temperature', methods=['GET','POST'])
def add_temperature():
    temp = request.form.get('temp')
    loc = request.form.get('loc')
    print(f"temp = {temp}, loc = {loc}")
    return render_template("form.html")


if __name__ == '__main__':
    server.run(debug=True)