from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

TEMP_FILE = "temperature.txt"
LIGHT_FILE = "light.txt"

# -------------------------------
# Initial Home Page
# -------------------------------
@app.route('/')
def home():
    return """
    <h1>Flask Server is Running ✅</h1>
    <p>Server connected successfully.</p>

    <h3>Available Services</h3>
    <ul>
        <li>/temperature/&lt;value&gt;  → Send temperature</li>
        <li>/light/&lt;value&gt;        → Send light intensity</li>
        <li><a href="/get_temperature">View Temperature Data</a></li>
        <li><a href="/get_light">View Light Data</a></li>
    </ul>
    """

# -------------------------------
# Receive Temperature
# -------------------------------
@app.route('/temperature/<float:temp>', methods=['GET', 'POST'])
def receive_temperature(temp):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(TEMP_FILE, "a") as f:
        f.write(f"{time} - {temp} °C\n")
    return f"Temperature {temp} °C received and stored"

# -------------------------------
# Receive Light Intensity
# -------------------------------
@app.route('/light/<int:light>', methods=['GET', 'POST'])
def receive_light(light):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LIGHT_FILE, "a") as f:
        f.write(f"{time} - {light} lux\n")
    return f"Light Intensity {light} lux received and stored"

# -------------------------------
# Get Temperature Readings
# -------------------------------
@app.route('/get_temperature')
def get_temperature():
    try:
        with open(TEMP_FILE, "r") as f:
            return f"<pre>{f.read()}</pre>"
    except:
        return "No temperature data available"

# -------------------------------
# Get Light Readings
# -------------------------------
@app.route('/get_light')
def get_light():
    try:
        with open(LIGHT_FILE, "r") as f:
            return f"<pre>{f.read()}</pre>"
    except:
        return "No light data available"

# -------------------------------
# Run Server
# -------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
