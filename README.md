# AWS-SFTP-PIPELINE

ITL (ingestion, transformation and loading) Datapipeline using SFTP's, lambdas, and a gluespark job, in order to save data into an rds.

This is the structure of the Data Pipeline:

![Alt text](screenshots_sftp-pipeline.jpg)

This were the processes and resources created to build the DataPipeline.
The lambdas and the Glue Job have IAM roles, in order to extract data from s3 and process it.

![Alt text](screenshots_s3.JPG)

![Alt text](screenshots_lambda.JPG)

![Alt text](screenshots lambda 2.JPG)

![Alt text](screenshots_glue.JPG)

![Alt text](screenshots_rds.JPG)
