with open("example.txt", "w") as f:
    f.write("Hello from AWS S3 Practical!")

import boto3

# Initialize S3 client
s3_client = boto3.client('s3')

bucket_name = "my-s3-practical-bucket"  # Replace with your actual bucket name
file_name = "example.txt"

# Upload a file
s3_client.upload_file(file_name, bucket_name, file_name)
print(f"{file_name} uploaded to {bucket_name}")

# Download the file
s3_client.download_file(bucket_name, file_name, "downloaded_" + file_name)
print(f"{file_name} downloaded from {bucket_name}")
