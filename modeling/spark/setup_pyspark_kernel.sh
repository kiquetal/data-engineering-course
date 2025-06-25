#!/bin/bash
# Script to set up a PySpark kernel for Jupyter

# Create a virtual environment for PySpark
python -m venv pyspark_env

# Activate the virtual environment
source pyspark_env/bin/activate

# Install necessary packages
pip install ipykernel pyspark==4.0.0 jupyter

# Create a Jupyter kernel for PySpark
python -m ipykernel install --user --name=pyspark_kernel --display-name="PySpark 4.0.0"

# Set environment variables for the kernel
mkdir -p ~/.jupyter/kernels/pyspark_kernel/

cat > ~/.jupyter/kernels/pyspark_kernel/kernel.json << EOF
{
 "argv": [
  "$(which python)",
  "-m",
  "ipykernel",
  "-f",
  "{connection_file}"
 ],
 "display_name": "PySpark 4.0.0",
 "language": "python",
 "env": {
  "PYSPARK_PYTHON": "$(which python)",
  "PYSPARK_DRIVER_PYTHON": "$(which python)",
  "SPARK_HOME": "$(pip show pyspark | grep Location | cut -d ' ' -f 2)/pyspark",
  "PYTHONPATH": "$(pip show pyspark | grep Location | cut -d ' ' -f 2)/pyspark/python:$(pip show pyspark | grep Location | cut -d ' ' -f 2)/pyspark/python/lib/py4j-0.10.9.7-src.zip",
  "PYSPARK_SUBMIT_ARGS": "--conf spark.driver.extraJavaOptions=-Djava.security.manager=allow --conf spark.executor.extraJavaOptions=-Djava.security.manager=allow pyspark-shell"
 }
}
EOF

echo "PySpark kernel setup is complete. You can now use the 'PySpark 4.0.0' kernel in Jupyter."
