# Aditi-Jain-Rearc-Quest-Assign

# Rearc Data Quest

Quest: [https://github.com/rearc-data/quest](https://github.com/rearc-data/quest).

![diagram](https://github.com/user-attachments/assets/1a4ced1b-f526-4037-afb1-aa25119411f7)

## Quest Solutions

### Step 1

- Link to data in S3:<br>

    [population.json](https://rerac-quest-s3-bucket.s3.amazonaws.com/population.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASNRSBQUB7EG3TP6Y%2F20250607%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20250607T130743Z&X-Amz-Expires=432000&X-Amz-SignedHeaders=host&X-Amz-Signature=6928b341ea4358e518b9c9e21e50dcb98ae9941d4a1ee4f55cebd03d637455a8), 
    [pr.class](https://rerac-quest-s3-bucket.s3.amazonaws.com/pr.class?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASNRSBQUB7EG3TP6Y%2F20250607%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20250607T130743Z&X-Amz-Expires=432000&X-Amz-SignedHeaders=host&X-Amz-Signature=837577a0a45f81f9b95d56dce69d30f8b814151070a59c2dbcb2839cfefcd172), 
    [pr.contacts](https://rerac-quest-s3-bucket.s3.amazonaws.com/pr.contacts?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASNRSBQUB7EG3TP6Y%2F20250607%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20250607T130743Z&X-Amz-Expires=432000&X-Amz-SignedHeaders=host&X-Amz-Signature=20f7f39972fdd50cc315c620eb6593a1a1cadc13083b040b0f3a04edef2b3826), 
    [pr.data.0.Current](https://rerac-quest-s3-bucket.s3.amazonaws.com/pr.data.0.Current?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASNRSBQUB7EG3TP6Y%2F20250607%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20250607T130743Z&X-Amz-Expires=432000&X-Amz-SignedHeaders=host&X-Amz-Signature=8024e63564d3e14df923b8b3b82485e7309ad30c54adffc7ef883b85a3b93870), 
    [pr.data.1.AllData](https://rerac-quest-s3-bucket.s3.amazonaws.com/pr.data.1.AllData?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASNRSBQUB7EG3TP6Y%2F20250607%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20250607T130743Z&X-Amz-Expires=432000&X-Amz-SignedHeaders=host&X-Amz-Signature=da678ae415f0ab7b8b2c02466e8511dad1721cf8224285980a3c16391f84af7f), 
    [pr.duration](https://rerac-quest-s3-bucket.s3.amazonaws.com/pr.duration?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASNRSBQUB7EG3TP6Y%2F20250607%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20250607T130743Z&X-Amz-Expires=432000&X-Amz-SignedHeaders=host&X-Amz-Signature=b3dbec11220eb83e8d8792131adc807062d8a4e04c9ba4adae584a6b9e3c40c1), 
    [pr.footnote](https://rerac-quest-s3-bucket.s3.amazonaws.com/pr.footnote?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASNRSBQUB7EG3TP6Y%2F20250607%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20250607T130743Z&X-Amz-Expires=432000&X-Amz-SignedHeaders=host&X-Amz-Signature=ab7da1642ee2defacf10f5d108275d5c2d417c8556fb1870c19510d6e04d1dfd), 
    [pr.measure](https://rerac-quest-s3-bucket.s3.amazonaws.com/pr.measure?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASNRSBQUB7EG3TP6Y%2F20250607%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20250607T130743Z&X-Amz-Expires=432000&X-Amz-SignedHeaders=host&X-Amz-Signature=780e0683ecd71b76fc325f0c1ccfec44b55b5f92ff88a544442ddfec055a0b7f), 
    [pr.period](https://rerac-quest-s3-bucket.s3.amazonaws.com/pr.period?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASNRSBQUB7EG3TP6Y%2F20250607%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20250607T130743Z&X-Amz-Expires=432000&X-Amz-SignedHeaders=host&X-Amz-Signature=c93879436b5004b5aa07943b01a4ee6dd329744b6977ed0a6d562d300cbd3963), 
    [pr.seasonal](https://rerac-quest-s3-bucket.s3.amazonaws.com/pr.seasonal?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASNRSBQUB7EG3TP6Y%2F20250607%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20250607T130743Z&X-Amz-Expires=432000&X-Amz-SignedHeaders=host&X-Amz-Signature=6b6a25126949e18213e236af8b97a163b1e5ee310154a317d499c4e9c314e3b8), 
    [pr.sector](https://rerac-quest-s3-bucket.s3.amazonaws.com/pr.sector?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASNRSBQUB7EG3TP6Y%2F20250607%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20250607T130743Z&X-Amz-Expires=432000&X-Amz-SignedHeaders=host&X-Amz-Signature=15b0d3006a26d0ffba0e9953ae942392a9b343b3baf1b5f678ed3f4619a6b7c7), 
    [pr.series](https://rerac-quest-s3-bucket.s3.amazonaws.com/pr.series?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASNRSBQUB7EG3TP6Y%2F20250607%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20250607T130743Z&X-Amz-Expires=432000&X-Amz-SignedHeaders=host&X-Amz-Signature=46feb07fe7834e37085bfc7a9dfe16dafba62ea5e953f93c2c735a6cd6c505a2), 
    [pr.txt](https://rerac-quest-s3-bucket.s3.amazonaws.com/pr.txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASNRSBQUB7EG3TP6Y%2F20250607%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20250607T130743Z&X-Amz-Expires=432000&X-Amz-SignedHeaders=host&X-Amz-Signature=3ac74d90ed63b6e3432b0a0d22fd91c3ddd69a9de44ced8a7634576664599542) 

- Source code: `part 1/data-ingestion.py`.

### Step 2

- Source code: `part 2/data-ingestion-population-data.py`.

### Step 3

- Source code in .ipynb file format and results: `part 3/Data_Analysis_Rearc.ipynb`.

### Step 4

- Source code of data pipeline infrastructure: `part 4/my-cdk-project/my_cdk_project/my_cdk_project_stack.py`.
