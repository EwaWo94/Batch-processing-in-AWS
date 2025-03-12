# file 2/3: posts

import requests
import json
import boto3

url = "https://api.stackexchange.com/2.3/posts"

params = {
    "pagesize": 100,
    "order": "desc",
    "sort": "activity",
    "site": "seasonedadvice",
    "filter": "!4yKf*M4h3tmeNXjfC4nAjePNhju*cEn5heXvg6",
    "access_token": "--",
    "key": "--",
}

data_list = []
page = 1

while True:
    # Update the page parameter
    params["page"] = page
    
    # Make a request to the API
    response = requests.get(url, params=params)
    data = response.json()
    
    # Extract data from the current page
    data_list.extend(data["items"])
    
    # Check if there are more pages
    if not data["has_more"]:
        break
    
    # Increment the page number
    page += 1

# Now data_list contains all data from multiple pages

# Convert data_list to JSON string
data_json = json.dumps(data_list)

# Upload data_json to S3
bucket_name = 'raw-allposts'
key = 'posts.json'
s3_client = boto3.client('s3')

response = s3_client.put_object(Bucket=bucket_name, Key=key, Body=data_json)
print(response)
