from flask import Flask, jsonify
from db import get_db_connection

app = Flask(__name__)

@app.delete('/moisture/<int:sensor_id>')
def delete_moisture(sensor_id):
    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM soil_moisture WHERE sensor_id=%s",
        (sensor_id,)
    )

    db.commit()
    cursor.close()
    db.close()

    return jsonify({"message": "Moisture data deleted"})

if __name__ == '__main__':
    app.run(port=4003, debug=True)
