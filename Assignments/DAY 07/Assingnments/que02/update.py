from flask import Flask, request, jsonify
from db import get_db_connection

app = Flask(__name__)

@app.put('/moisture/<int:sensor_id>')
def update_moisture(sensor_id):
    data = request.json
    moisture = data['moisture_level']

    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute(
        "UPDATE soil_moisture SET moisture_level=%s WHERE sensor_id=%s",
        (moisture, sensor_id)
    )

    db.commit()
    cursor.close()
    db.close()

    return jsonify({"message": "Moisture data updated"})

if __name__ == '__main__':
    app.run(port=4002, debug=True)
