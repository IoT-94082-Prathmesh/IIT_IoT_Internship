from flask import Flask, request, jsonify
from db import get_db_connection

app = Flask(__name__)
@app.get('/')
def home():
    return """
    <h2> SOIL MOISTURE API </h2>
    """
@app.post('/moisture')
def add_moisture():
    data = request.json
    moisture = data['moisture_level']

    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO soil_moisture (moisture_level) VALUES (%s)",
        (moisture,)
    )

    db.commit()
    cursor.close()
    db.close()

    return jsonify({"message": "Moisture data inserted"})

if __name__ == '__main__':
    app.run(port=4000, debug=True)
