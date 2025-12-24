from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)

@app.get('/')
def home():
    return """
    <h2>IoT Sensor Readings API</h2>
    """

# ---------- MySQL Connection ----------
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_mysql_password",
        database="iot_data"
    )

# ---------- CREATE (Insert sensor reading) ----------
@app.post('/sensor')
def add_sensor():
    data = request.json
    temperature = data['temperature']
    humidity = data['humidity']

    db = get_db_connection()
    cursor = db.cursor()

    query = """
    INSERT INTO sensor_readings (temperature, humidity)
    VALUES (%s, %s)
    """
    cursor.execute(query, (temperature, humidity))
    db.commit()

    cursor.close()
    db.close()

    return jsonify({"message": "Sensor data added successfully"}), 201


# ---------- READ (Get all sensor readings) ----------
@app.get('/sensor')
def get_all_sensors():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM sensor_readings")
    records = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(records)


# ---------- READ by ID ----------
@app.get('/sensor/<int:id>')
def get_sensor_by_id(id):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM sensor_readings WHERE id=%s", (id,))
    record = cursor.fetchone()

    cursor.close()
    db.close()

    if record:
        return jsonify(record)
    else:
        return jsonify({"error": "Record not found"}), 404


# ---------- UPDATE ----------
@app.put('/sensor/<int:id>')
def update_sensor(id):
    data = request.json
    temperature = data['temperature']
    humidity = data['humidity']

    db = get_db_connection()
    cursor = db.cursor()

    query = """
    UPDATE sensor_readings
    SET temperature=%s, humidity=%s
    WHERE id=%s
    """
    cursor.execute(query, (temperature, humidity, id))
    db.commit()

    cursor.close()
    db.close()

    return jsonify({"message": "Sensor data updated successfully"})


# ---------- DELETE ----------
@app.delete('/sensor/<int:id>')
def delete_sensor(id):
    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("DELETE FROM sensor_readings WHERE id=%s", (id,))
    db.commit()

    cursor.close()
    db.close()

    return jsonify({"message": "Sensor data deleted successfully"})


# ---------- WEB SERVICE: Threshold Value ----------
# Example:
# /sensor/threshold?type=temperature&value=30
# /sensor/threshold?type=humidity&value=50
@app.get('/sensor/threshold')
def sensor_threshold():
    sensor_type = request.args.get('type')
    value = float(request.args.get('value'))

    if sensor_type not in ['temperature', 'humidity']:
        return jsonify({"error": "Invalid type"}), 400

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    query = f"SELECT * FROM sensor_readings WHERE {sensor_type} < %s"
    cursor.execute(query, (value,))
    records = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(records)


# ---------- Run Server ----------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
