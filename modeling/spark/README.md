# Apache Spark Project Setup

This guide will help you set up a new Apache Spark project using **Python** (PySpark), which is widely used, robust, and has excellent community support.

## Prerequisites
- Python 3.8 or newer
- Java 8 or newer (for Spark)
- pip (Python package manager)
- Docker (for containerized execution)

## Steps to Initialize a PySpark Project

1. **Create and activate a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install PySpark:**
   ```bash
   pip install pyspark
   ```

3. **Verify installation:**
   ```bash
   python -c "import pyspark; print(pyspark.__version__)"
   ```

4. **Create your first Spark application:**
   - Create a file named `app.py` with the following content:
     ```python
     from pyspark.sql import SparkSession

     spark = SparkSession.builder.appName("MySparkApp").getOrCreate()
     df = spark.createDataFrame([(1, "foo"), (2, "bar")], ["id", "value"])
     df.show()
     spark.stop()
     ```

5. **Run your Spark application:**
   ```bash
   python app.py
   ```

## Running with Docker

For a secure, high-performance, and easy-to-run environment, follow these steps:

1. **Build the Docker image:**
   ```bash
   docker build -t spark-app .
   ```

2. **Run the Spark application in a container:**
   ```bash
   docker run -it --rm -v $(pwd):/app spark-app python app.py
   ```

This containerized approach ensures consistent execution across environments and proper isolation of dependencies.

## Advanced Usage

For more complex scenarios:

- **Run with custom configurations:**
  ```bash
  docker run -it --rm -v $(pwd):/app spark-app python app.py --conf "spark.executor.memory=2g"
  ```

- **Interactive development with Jupyter notebooks:**
  - Add Jupyter to the Dockerfile and expose the appropriate port
  - Run with: `docker run -it --rm -p 8888:8888 -v $(pwd):/app spark-jupyter`

## Additional Resources
- [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/)
- [Apache Spark Official Site](https://spark.apache.org/)

---

The included `app.py` demonstrates various Spark operations including DataFrame creation, transformations, SQL queries, and expressions.
