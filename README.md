This project simulates an IoT sensor that publishes temperature and humidity data to AWS IoT Core via MQTT. If the temperature exceeds a threshold, an SNS alert is triggered. All data is stored in Amazon S3 using a Lambda function invoked by an IoT Rule.

⚙️ Architecture
java
Copy
Edit
Simulated Sensor (Python script)
        ↓ MQTT
     AWS IoT Core
        ↓ IoT Rule (SQL + Condition)
     AWS Lambda (store payload to S3)
        ↓
     SNS Topic (alert if temperature > 25°C)
        ↓
     Amazon S3 (stores JSON files)
🧰 Components
Component	Details
MQTT Topic	sensor/temp
IoT Core Rule	SQL rule: SELECT * FROM 'sensor/temp'
AWS Lambda	Parses payload, stores to S3, triggers SNS if temperature > 25
S3 Bucket	simulatedtempiot
SNS Topic	hightempalert (with email subscription for notifications)
Device ID	simulatedSensor001
