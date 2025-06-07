import boto3
import requests
from bs4 import BeautifulSoup
import os

# User-Agent header to comply with BLS policy
HEADERS = {
    "User-Agent": "email_id"
}

# Get file list from the website
def get_files_from_website(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    files = []

    for link in soup.find_all("a"):
        name = link.get_text()
        if name != "[To Parent Directory]":
            files.append(name.strip())
    return files

# Get file list from S3
def get_files_from_s3(bucket):
    return [obj.key for obj in bucket.objects.all()]

# Upload a file to S3
def upload_file_to_s3(bucket, key, content):
    bucket.put_object(Key=key, Body=content)
    print(f"Uploaded/Updated: {key}")

# Delete a file from S3
def delete_file_from_s3(bucket, key):
    bucket.Object(key).delete()
    print(f"Deleted: {key}")

# Compare file content
def is_file_different(bucket, key, new_content):
    try:
        existing = bucket.Object(key).get()['Body'].read()
        return existing != new_content
    except:
        return True

def lambda_handler(event, context):
    S3_BUCKET = os.environ.get("S3_BUCKET_NAME")
    DATA_URL = "https://download.bls.gov/pub/time.series/pr/"
    POP_API = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(S3_BUCKET)

    # Step 1: Get lists
    website_files = set(get_files_from_website(DATA_URL))
    s3_files = set(get_files_from_s3(bucket))

    # Step 2: Add or update files
    for file_name in website_files:
        file_url = DATA_URL + file_name
        file_data = requests.get(file_url, headers=HEADERS).content

        if file_name not in s3_files or is_file_different(bucket, file_name, file_data):
            upload_file_to_s3(bucket, file_name, file_data)

    # Step 3: Remove files no longer on the website (except population.json)
    files_to_delete = s3_files - website_files
    for file in files_to_delete:
        if file != "population.json": 
            delete_file_from_s3(bucket, file)

    # Step 4: Save population data from API
    try:
        pop_response = requests.get(POP_API, headers=HEADERS)
        if pop_response.status_code == 200:
            upload_file_to_s3(bucket, "population.json", pop_response.text)
        else:
            print("API call failed:", pop_response.status_code)
    except Exception as e:
        print("Error fetching population API:", str(e))

    return "Sync complete."
