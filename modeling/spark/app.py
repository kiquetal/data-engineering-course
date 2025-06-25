#!/usr/bin/env python3
"""
Example Spark application demonstrating SparkSession usage
with the latest version of Apache Spark.
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, expr
import os
import tempfile

def main():
    """
    Main function to demonstrate SparkSession capabilities
    """
    # IMPORTANT FOR LOCAL TESTING:
    # If you encounter permission errors, either:
    # 1. Change ownership of the artifacts folder: chmod -R 777 artifacts/
    # 2. Or uncomment the following lines to use a temporary directory:
    # tmp_dir = tempfile.mkdtemp()
    # os.environ['SPARK_LOCAL_DIRS'] = tmp_dir

    # Create a SparkSession
    spark = (SparkSession.builder
             .appName("SparkLatestVersionDemo")
             .config("spark.sql.shuffle.partitions", "2")  # Performance config for small datasets
             .config("spark.executor.memory", "1g")
             .config("spark.driver.memory", "1g")
             # Fix for security manager issue in Spark 4.0.0
             .config("spark.driver.extraJavaOptions", "-Djava.security.manager=allow")
             .config("spark.executor.extraJavaOptions", "-Djava.security.manager=allow")

             # UNCOMMENT THESE LINES FOR TEMP DIRECTORY USAGE:
             # .config("spark.local.dir", tmp_dir)
             # .config("spark.worker.dir", tmp_dir)
             # .config("spark.sql.warehouse.dir", f"{tmp_dir}/spark-warehouse")

             .master("local[*]")  # Explicitly set to local mode
             .getOrCreate())

    print(f"Spark version: {spark.version}")

    # Sample data
    data = [
        ("Alice", 34, "Data Engineer"),
        ("Bob", 45, "Data Scientist"),
        ("Charlie", 29, "ML Engineer"),
        ("Diana", 37, "Data Analyst"),
        ("Eve", 31, "Software Engineer")
    ]

    # Create DataFrame
    columns = ["name", "age", "job_title"]
    df = spark.createDataFrame(data, columns)

    print("Sample DataFrame:")
    df.show()

    # Basic transformations
    print("\nBasic transformations:")
    (df.select("name", "job_title", col("age").cast("int"))
       .filter(col("age") > 30)
       .withColumn("department", lit("Data"))
       .orderBy("age")
       .show())

    # SQL query
    print("\nUsing SQL query:")
    df.createOrReplaceTempView("employees")
    spark.sql("""
        SELECT name, job_title, age
        FROM employees
        WHERE age > 35
        ORDER BY age DESC
    """).show()

    # DataFrame operations with expressions
    print("\nUsing expressions:")
    (df.withColumn("experience_category",
                  expr("CASE WHEN age < 30 THEN 'Junior' " +
                       "WHEN age <= 40 THEN 'Mid-level' " +
                       "ELSE 'Senior' END"))
       .show())

    # Stop the SparkSession
    spark.stop()
    print("SparkSession closed successfully")

    # UNCOMMENT FOR TEMP DIRECTORY CLEANUP:
    # import shutil
    # shutil.rmtree(tmp_dir)
    # print(f"Cleaned up temporary directory: {tmp_dir}")

if __name__ == "__main__":
    main()
