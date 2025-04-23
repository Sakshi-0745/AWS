import boto3

def list_active_services():
    client = boto3.client('ce')  # Cost Explorer
    response = client.get_dimension_values(
        Dimension='SERVICE',
        TimePeriod={
            'Start': '2024-03-01',
            'End': '2025-05-01'
        }
    )
    services = [item['Value'] for item in response['DimensionValues']]
    return services

def list_available_regions():
    ec2_client = boto3.client('ec2')
    regions = ec2_client.describe_regions()['Regions']
    return [region['RegionName'] for region in regions]

if __name__ == "__main__":
    print("Fetching active AWS services...")
    active_services = list_active_services()
    print(f"Active Services ({len(active_services)}):\n", active_services)

    print("\nFetching available AWS regions...")
    regions = list_available_regions()
    print(f"Available Regions ({len(regions)}):\n", regions)
