from flask import Flask, request, jsonify
from db import get_db_connection

app = Flask(__name__)

@app.get('/moisture/threshold')
def moisture_threshold():
    value = float(request.args.get('value'))

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM soil_moisture WHERE moisture_level < %s",
        (value,)
    )

    records = cursor.fetchall()
    cursor.close()
    db.close()

    return jsonify(records)

if __name__ == '__main__':
    app.run(port=4004, debug=True)
