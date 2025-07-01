import boto3

def upload_to_s3(file_path: str, bucket: str, key: str):
    s3 = boto3.client("s3")
    s3.upload_file(file_path, bucket, key)
    return f"https://{bucket}.s3.amazonaws.com/{key}"
