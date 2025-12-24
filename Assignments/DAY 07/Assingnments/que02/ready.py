from flask import Flask, jsonify
from db import get_db_connection

app = Flask(__name__)

@app.get('/moisture')
def get_all_moisture():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM soil_moisture")
    records = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(records)

if __name__ == '__main__':
    app.run(port=4001, debug=True)
