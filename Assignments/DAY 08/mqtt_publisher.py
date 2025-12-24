# install library/module for mqtt
#   pip install paho-mqtt

# import mqtt module
import paho.mqtt.client as mqtt

def on_publish(client, userdata, mid, reason_code, properties):
    print("message is published")

# creat a client to publish data
publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# add on_publish into our publisher
publisher.on_publish = on_publish

# send connect message to publisher
publisher.connect("localhost")

# publish the message
publisher.publish("sensor/ldr", 2048)

# disconnect from broker
publisher.disconnect()