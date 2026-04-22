
import boto3
s3 = boto3.client('s3')
sns_client = boto3.client('sns', region_name='us-east-1')

def lambda_handler(event, context):
    paginator = s3.get_paginator('list_objects_v2')

    for page in paginator.paginate(Bucket='autovault-source-david-odesomi'):
        if 'Contents' in page:
            for obj in page['Contents']:
                key = obj['Key']
                copy_source = {'Bucket': 'autovault-source-david-odesomi', 'Key': key}
                s3.copy_object(CopySource=copy_source, Bucket='backedup-file-important', Key=key)
                # s3.delete_object(Bucket='source-bucket', Key=key)
    sns_client.publish(
    TopicArn='arn:aws:sns:us-east-1:352100722652:AutoVault',
    Message=f'Complete backup from autovault-source-david-odesomi'
    )