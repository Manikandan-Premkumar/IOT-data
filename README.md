This project simulates an IoT sensor that publishes temperature and humidity data to AWS IoT Core via MQTT. If the temperature exceeds a threshold, an SNS alert is triggered. All data is stored in Amazon S3 using a Lambda function invoked by an IoT Rule.

🔧 Architecture
Sensor → AWS IoT Core → Lambda → 
    ├── S3 (store JSON data)
    └── SNS (send alert if temperature > threshold)

✅ IAM Permissions Needed
s3:PutObject to the specific bucket

sns:Publish to the topic

logs:* for debugging
     
| Component        | Details                                                                 |
|------------------|-------------------------------------------------------------------------|
| MQTT Topic       | `sensor/temp`                                                           |
| IoT Core Rule    | SQL rule: `SELECT * FROM 'sensor/temp'`                                 |
| AWS Lambda       | Parses payload, stores to S3, triggers SNS if `temperature > 25`        |
| S3 Bucket        | `simulatedtempiot`                                                      |
| SNS Topic        | `hightempalert` (email alert)                                           |
| Device ID        | `simulatedSensor`                                                    |



SNS alert received via Mail
![image](https://github.com/user-attachments/assets/441dd849-e314-4692-901a-3b24d45127ab)

