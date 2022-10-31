import boto3
import os

os.environ['AWS_DEFAULT_REGION'] = 'us-west-2'
os.environ['AWS_PROFILE'] = "default"

ssm_client = boto3.client("ssm")

new_string_parameter = ssm_client.put_parameter(
    Name='apiToken',
    Description='this my token',
    Value='8a1f9d6cc8720d795d34e22f6c49761ff2fca62c',
    Type='SecureString',
    Overwrite=True,
    Tier='Standard')

print(
    f"String Parameter created with version {new_string_parameter['Version']} and Tier {new_string_parameter['Tier']}"
)