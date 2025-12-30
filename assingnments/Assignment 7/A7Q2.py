from flask import Flask, request
from datetime import datetime

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"


@server.post('/soil_moisture')
def create_soil_moisture():
    sensor_id = request.form.get('sensor_id')
    moisture_level = request.form.get('moisture_level')
    date_time_str = request.form.get('date_time')

    date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")

    query = f"""
    INSERT INTO soil_moisture (sensor_id, moisture_level, date_time)
    VALUES ({sensor_id}, {moisture_level}, '{date_time}');
    """

    executeQuery(query=query)

    return "soil_moisture is added successfully"


@server.get('/soil_moisture')
def retrieve_soil_moisture():
    query = "SELECT * FROM soil_moisture;"
    query1 = "SELECT * FROM soil_moisture WHERE moisture_level < 56;"

    data = executeSelectQuery(query=query)
    data1 = executeSelectQuery(query=query1)

    return f"soil_moisture: {data}\n\n\n  threshold value: {data1}"


@server.put('/soil_moisture')
def update_soil_moisture():
    sensor_id = request.form.get('sensor_id')
    moisture_level = request.form.get('moisture_level')

    query = f"""
    UPDATE soil_moisture
    SET moisture_level = {moisture_level}
    WHERE sensor_id = {sensor_id};
    """

    executeQuery(query=query)

    return "soil_moisture is updated successfully"


@server.delete('/soil_moisture')
def delete_soil_moisture():
    sensor_id = request.form.get('sensor_id')

    query = f"DELETE FROM soil_moisture WHERE sensor_id = {sensor_id};"

    executeQuery(query=query)

    return "soil_moisture is deleted successfully"


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)