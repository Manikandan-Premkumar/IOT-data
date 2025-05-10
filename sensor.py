# File: pi_sensor_publisher.py
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import time
import random

# AWS IoT Core Configuration
ENDPOINT = "*.iot.eu-north-1.amazonaws.com"
CLIENT_ID = "tempsensor"
PATH_CERT = "./certs/certificate.pem.crt"
PATH_KEY = "./certs/private.pem.key"
PATH_ROOT = "./certs/AmazonRootCA1.pem"

myMQTTClient = AWSIoTMQTTClient(CLIENT_ID)
myMQTTClient.configureEndpoint(ENDPOINT, 8883)
myMQTTClient.configureCredentials(PATH_ROOT, PATH_KEY, PATH_CERT)

# Connect and publish
myMQTTClient.connect()
while True:
    sensor_data = {
        "device_id": CLIENT_ID,
        "timestamp": int(time.time()),
        "temperature": round(random.uniform(20.0, 30.0)),  # Simulated data
        
    } 
    myMQTTClient.publish("sensor/temp", json.dumps(sensor_data), 1)
    time.sleep(10)  # Send every 5 minutes
