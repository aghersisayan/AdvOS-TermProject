#!/bin/bash

# Variables
SPARK_DIR="/opt/spark" # Apache Spark directory on the EC2 instance
EMRFS_SCRIPT="trainWithEmrfs.py" # Name of the training script with EMRFS
HDFS_SCRIPT="trainWithHdfs.py" # Name of the training script with HDFS
OUTPUT_FILE="performance_results.txt" # Name of the file to save the results

# Fix for saving results
results=()

# Function to run the training script and save the results
run_training_script() {
     script=$1
     hyperparameters=$2

     # Run the training script and save the results to a variable
     result=$(spark-submit $SPARK_DIR/$script $hyperparameters)

     # Get start and end time
     start_time=$(date +"%Y-%m-%d %H:%M:%S")
     end_time=$(date +"%Y-%m-%d %H:%M:%S")

     # Add the results to the array
     results+=("$start_time" "$end_time" "$hyperparameters" "$result")
}

# Run the training script with different hyperparameter values and save the results
run_training_script $EMRFS_SCRIPT "epochs=5"
run_training_script $EMRFS_SCRIPT "epochs=10"
run_training_script $EMRFS_SCRIPT "epochs=15"
run_training_script $HDFS_SCRIPT "epochs=5"
run_training_script $HDFS_SCRIPT "epochs=10"
run_training_script $HDFS_SCRIPT "epochs=15"

# Save results to file
echo "${results[@]}" > $OUTPUT_FILE