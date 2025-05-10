import json
import boto3
import datetime

s3 = boto3.client('s3')
sns = boto3.client('sns')

BUCKET_NAME = 'simulatedtemp'
TOPIC_ARN = 'arn:aws:sns:*'

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))

    payload = event
    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H-%M-%S')
    payload['timestamp'] = timestamp

    object_key = f"sensor_data/{timestamp}.json"

    try:
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=object_key,
            Body=json.dumps(payload),
            ContentType='application/json'
        )
    except Exception as e:
        print(f"S3 put_object failed: {str(e)}")

    try:
        temp = float(payload.get("temperature", 0))
        if temp > 25:
            sns.publish(
                TopicArn=TOPIC_ARN,
                Subject="🔥 High Temp Alert",
                Message=f"Temperature is {temp}°C at {timestamp}"
            )
    except Exception as e:
        print("Temperature parsing or alert failed:", str(e))

    return {
        'statusCode': 200,
        'body': 'Data stored and alert handled'
    }
