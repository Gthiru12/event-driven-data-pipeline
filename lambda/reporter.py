import boto3
import csv
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

TABLE_NAME = 'event-data'
REPORT_BUCKET = 'event-report-bucket-demo'

def lambda_handler(event, context):
    table = dynamodb.Table(TABLE_NAME)
    response = table.scan()

    items = response.get('Items', [])

    total_events = len(items)
    total_value = sum(int(item.get('value', 0)) for item in items)

    report_name = f"daily-report-{datetime.now().date()}.csv"
    file_path = f"/tmp/{report_name}"

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Total Events", "Total Value"])
        writer.writerow([total_events, total_value])

    s3.upload_file(file_path, REPORT_BUCKET, report_name)

    return {
        "statusCode": 200,
        "body": "Daily report generated"
    }





