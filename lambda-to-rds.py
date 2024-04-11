import boto3
import csv
import pymysql


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    rds_host = 'xxxxxxx.com'
    db_username = 'admin'
    db_password = 'xxxxxxxxxxxxxxxxxxx'
    db_name = 'databasename'    
    
    conn = pymysql.connect(host=rds_host,
                             user=db_username,
                             password=db_password,
                             database=db_name,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor,
                             connect_timeout=80)
    cursor = conn.cursor()
    
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    data = response['Body'].read().decode('utf-8').split('\n')
    
    csv_reader = csv.reader(data)
    next(csv_reader)
    
    for row in csv_reader:
        # Insert row into RDS   TIENES QUE AGARRAR EL ORDEN DEL CSV PARA METERLO AL SQL
        cursor.execute("INSERT INTO Iris_dataset1 (Id, sepal_length, sepal_width, petal_length, petal_width, Volumen_Iris, class) VALUES (%s,%s,%s,%s,%s,%s,%s)", row)
        conn.commit()
    
    cursor.close()
    conn.close()
