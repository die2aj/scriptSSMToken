import boto3
import os
import requests
import json

os.environ['AWS_DEFAULT_REGION'] = 'us-west-2'
os.environ['AWS_PROFILE'] = "default"

ssm_client = boto3.client("ssm")

response = requests.get("https://api.themoviedb.org/3/authentication/token/new?api_key=725374be1608b260795fe92a785532b0")
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


new_string_parameter = ssm_client.put_parameter(
    Name='apiToken',
    Description='this my token',
    Value=response.json().get("request_token"),
    Type='SecureString',
    Overwrite=True,
    Tier='Standard')

print(
    f"String Parameter created with version {new_string_parameter['Version']} and Tier {new_string_parameter['Tier']}"
)