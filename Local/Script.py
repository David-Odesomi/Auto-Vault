import boto3
import os 

s3 = boto3.client('s3')
s3_client = boto3.client('s3', region_name='us-east-1')
s3_client.create_bucket(Bucket='autovault-source-david-odesomi')
s3.put_bucket_versioning(
    Bucket='autovault-source-david-odesomi',
    VersioningConfiguration={
        'Status': 'Enabled'
    }
)

local_path = "/Users/David/Desktop/important_files"

def local_upload():
    for file in os.listdir(local_path):
        file = os.path.join(local_path, file)
        s3.upload_file(
        Filename=file, 
        Bucket='autovault-source-david-odesomi', 
        Key=os.path.basename(file)
)
    def notify_advanced(title, subtitle, message):
        cmd = f'display notification "{message}" subtitle "{subtitle}" with title "{title}" sound name "Glass"'
        os.system(f"osascript -e '{cmd}'")

    notify_advanced(f"Backup Upload of ",{local_path}," completed.")

local_upload()