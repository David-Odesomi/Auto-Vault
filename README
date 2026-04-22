# AutoVault 🗄️

An automated cloud backup system with email notifications, built on AWS.

## How It Works

A Python script runs on a cron schedule on your local machine, uploading files 
from a specified directory to an S3 source bucket. An EventBridge rule triggers 
a Lambda function on a set schedule, which copies all objects from the source 
bucket into a backup bucket. Once the backup completes, an SNS notification is 
sent to any confirmed email subscribers. Older backups are automatically moved 
to Glacier storage after 30 days via an S3 lifecycle policy.

Execution logs are available in AWS CloudWatch.

## Tools Used

- AWS S3
- AWS Lambda
- AWS EventBridge
- AWS SNS
- AWS CloudWatch
- Python
- Linux (cron)

## Setup

1. Add your source directory path to the local script
2. Create your S3 source and backup buckets
3. Deploy the Lambda function with S3 and SNS IAM permissions
4. Create an SNS topic and confirm your email subscription
5. Schedule the Lambda with an EventBridge rule