import json
import boto3
from datetime import datetime



dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('FinanceMigrationLogs')


def lambda_handler(event, context):
    # TODO implement
    try: 
        resource = event['Records'][0]
        bucket_name = resource['s3']['bucket']['name']
        file_name = resource['s3']['object']['key']
        file_size = resource['s3']['object']['size']

        timestamp = datetime.utcnow().isoformat()

        table.put_item(
            Item = {
                'Timestamp': timestamp,
                'FileName': file_name,
                'FileSize': file_size,
                'BucketName': bucket_name
                

            }
        )
        print(f"Report: Logs recorded successfully for {file_name}")
        return {
            'statusCode': 200,
            'body': json.dumps(f'Logs recorded for {file_name}')
        }
    except Exception as e:
        print(f'Error logging file {str(e)}')
        raise e

