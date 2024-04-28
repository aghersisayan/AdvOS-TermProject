# DistilBERT Model Training Project with Apache Spark on AWS

This project aims to perform language model tuning using the DistilBERT architecture with Apache Spark on AWS. The goal is to train language models using SST2 (Stanford Sentiment Treebank 2) benchmark data sets, stored in an Amazon S3 bucket, and evaluate the performance of the models using metrics such as the F-score.

## Project Requirements:
Sign in to an Amazon Web Services (AWS) account with permissions to create and manage EC2 instances, EMR clusters, and S3 buckets.
Basic knowledge of AWS, Apache Spark, and Hugging Face Transformers library.
##Project Settings:
#### Creating S3 Bucket:
Create a bucket in Amazon S3 to store the SST2 benchmark data sets and training results.

`aws s3 mb s3://your-bucket-name`

#### EC2 instance configuration:
Create an EC2 instance on AWS with the Amazon Linux image.
Assigns an IAM role to the EC2 instance with permissions to access the S3 bucket. You can use the following JSON for bucket permissions:

      {
          "Version": "2012-10-17",
          "Statement": [
              {
                  "Effect": "Allow",
                  "Action": [
                      "s3:GetObject",
                      "s3: Set Object"
                  ],
                  "Resource": [
                      "arn:aws:s3:::name-of-your-bucket/*"
                  ]
              }
          ]
      }
#### Apache Spark installation and configuration:
Download and install Apache Spark on the EC2 instance.
Configure environment variables to access Spark from any location on the instance.
Run the following command to run the Spark configuration script:

`/opt/spark/bin/spark-submit setup_spark.py`

## Project execution:
#### Uploading the dataset to S3:
Copy the SST2 data set to the S3 bucket created above. You can use the following command to copy the data from your local to the S3 bucket:

`aws s3 cp data/ s3://your-bucket-name/dataset/ --recursive`

#### DistilBERT Model Training:
Run the training scripts trainWithEmrfs.py and trainWithHdfs.py from the EC2 instance.
#### Performance evaluation:
Use the following command to run the evaluation script and obtain performance metrics:

`python evaluate_model.py`

#### Evaluation Charts:
Use the following command to run the Matplotlib scripts and generate comparison plots:

`python generate_graphs.py`

## References

Apache Spark Documentation
Hugging Face Transformers Documentation
Amazon Web Services Documentation
