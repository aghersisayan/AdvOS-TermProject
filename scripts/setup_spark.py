#!/bin/bash

wget https://archive.apache.org/dist/spark/spark-x.y.z/spark-x.y.z-bin-hadoopx.y.tgz
tar -xzvf spark-x.y.z-bin-hadoopx.y.tgz
mv spark-x.y.z-bin-hadoopx.y /opt/spark
rm spark-x.y.z-bin-hadoopx.y.tgz

echo 'export SPARK_HOME=/opt/spark' >> ~/.bashrc
echo 'export PATH=$PATH:$SPARK_HOME/bin' >> ~/.bashrc
echo 'export PYSPARK_PYTHON=/usr/bin/python3' >> ~/.bashrc
echo 'export PYSPARK_DRIVER_PYTHON=/usr/bin/python3' >> ~/.bashrc
source ~/.bashrc