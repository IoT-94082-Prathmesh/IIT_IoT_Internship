from sever import app, get_db_connection
from flask import request, jsonify

@app.put('/sensor/apply_threshold')
def apply_threshold():
    threshold = float(request.args.get('value'))

    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("""
        UPDATE sensor_readings
        SET status = 'LOW'
        WHERE temperature < %s
    """, (threshold,))

    cursor.execute("""
        UPDATE sensor_readings
        SET status = 'NORMAL'
        WHERE temperature >= %s
    """, (threshold,))

    db.commit()
    cursor.close()
    db.close()

    return jsonify({"message": "MySQL table updated using threshold"})
