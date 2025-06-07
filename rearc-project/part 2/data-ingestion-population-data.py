import boto3
import requests

S3_BUCKET_NAME = "rerac-quest-s3-bucket" 
POP_API = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"

# Upload a file to S3
def upload_file_to_s3(bucket, key, content):
    bucket.put_object(Key=key, Body=content)
    print(f"Uploaded/Updated: {key}")

def main():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(S3_BUCKET_NAME)

    # Fetch population data from API and upload to S3
    try:
        pop_response = requests.get(POP_API)
        if pop_response.status_code == 200:
            upload_file_to_s3(bucket, "population.json", pop_response.text)
        else:
            print("API call failed with status code:", pop_response.status_code)
    except Exception as e:
        print("Error fetching population API:", str(e))

    print("Sync complete.")

if __name__ == "__main__":
    main()
