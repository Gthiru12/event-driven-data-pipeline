import json
import boto3
import uuid

s3 = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("event-data")

def lambda_handler(event, context):
    print("EVENT RECEIVED:", event)

    if "Records" not in event:
        print("No S3 records found. Exiting.")
        return

    for record in event["Records"]:
        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]

        print(f"Reading file {key} from bucket {bucket}")

        response = s3.get_object(Bucket=bucket, Key=key)
        body = response["Body"].read().decode("utf-8")
        data = json.loads(body)

        table.put_item(
            Item={
                "event_id": str(uuid.uuid4()),
                "source": data.get("source"),
                "value": data.get("value")
            }
        )

    print("Item successfully inserted into DynamoDB")

