# Use the official Python image with slim variant for smaller size
FROM python:3.11-slim

# Set environment variables for security and performance
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    SPARK_VERSION=4.0.0 \
    HADOOP_VERSION=3 \
    PYTHONPATH=/opt/spark/python \
    PYSPARK_PYTHON=python3

# Install Java (required for Spark), wget, and other dependencies
RUN apt-get update && \
    apt-get install -y default-jre wget ca-certificates curl procps && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME based on default-jre installation path
ENV JAVA_HOME=/usr/lib/jvm/default-java

# Install Spark with the exact version match
RUN mkdir -p /opt && \
    cd /tmp && \
    curl -fsSL --retry 3 --retry-delay 3 https://dlcdn.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -o spark.tgz && \
    tar -xzf spark.tgz -C /opt && \
    rm spark.tgz && \
    ln -s /opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} /opt/spark

ENV SPARK_HOME=/opt/spark
ENV PATH="$PATH:/opt/spark/bin:/opt/spark/sbin"

# Create working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt ./

# Create a filtered requirements file without any PySpark related packages
RUN grep -v -E "^pyspark|^py4j|pyspark-stubs" requirements.txt > requirements.filtered.txt && \
    pip install --no-cache-dir -r requirements.filtered.txt && \
    # Then install the exact PySpark version
    pip install --no-cache-dir pyspark==${SPARK_VERSION} && \
    # Verify the installation
    python -c "import pyspark; print(f'Successfully installed PySpark {pyspark.__version__}')"

# Copy application code
COPY . .

# Default command
CMD ["python", "app.py"]
