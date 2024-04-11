
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.getOrCreate()


def main():
    ## @params: [JOB_NAME]
    args = getResolvedOptions(sys.argv, ["VAL1"])
    file_names=args['VAL1'].split(',')
    df = spark.read.csv(file_names, header = True)
    
    df = df.withColumn("Volumen_Iris", (df.SepalWidthCm*df.PetalLengthCm/df.SepalLengthCm*df.PetalWidthCm)).withColumn("Classes",F.regexp_replace(F.col("Species"), "[-]", ""))
    
    df = df.drop("Species")
    
    df.repartition(1).write.mode('append').csv("s3a://aws-codestar-us-east-1-691119770807/publish/")

main()
