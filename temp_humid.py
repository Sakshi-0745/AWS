import boto3
import json
import time

# Initialize an IoT Data client
iot_client = boto3.client('iot-data', region_name='ap-south-1', endpoint_url='https://a337spuevry2az-ats.iot.ap-south-1.amazonaws.com')

# Define topic and payload
topic = "iot/test"
payload = {
    "temperature": 25.5,
    "humidity": 60
}

# Publish data to the IoT Core topic
for _ in range(10):
    response = iot_client.publish(
        topic=topic,
        qos=1,
        payload=json.dumps(payload)
    )
    print("Data published to topic:", payload)
    time.sleep(5)
