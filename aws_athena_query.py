import boto3
import time
from botocore.exceptions import ClientError

# Athena client
athena_client = boto3.client('athena', region_name='ap-south-1')  # e.g., 'us-east-1'

# Your details
database = "edrdatabase"
table = "synthetic_fraud_dataset_csv"
output_bucket = "my-s3-practical-bucket"  # Ensure this bucket exists
query = f"SELECT * FROM {database}.{table} LIMIT 10;"
output_location = f"s3://{output_bucket}/athena-results/"

# Start query
response = athena_client.start_query_execution(
    QueryString=query,
    QueryExecutionContext={"Database": database},
    ResultConfiguration={"OutputLocation": output_location}
)

# Fetch execution ID
query_execution_id = response["QueryExecutionId"]
print("Query started with ID:", query_execution_id)

# Wait for result
while True:
    status = athena_client.get_query_execution(QueryExecutionId=query_execution_id)
    state = status['QueryExecution']['Status']['State']
    if state in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
        break
    print("Query is still running...")
    time.sleep(2)

# Check final state
if state == 'SUCCEEDED':
    print("Query succeeded!")
    print("Result file:", f"{output_location}{query_execution_id}.csv")
else:
    print("Query failed or was cancelled:", state)
