import matplotlib.pyplot as plt
import numpy as np

# Load data from results file
data_emrfs = np.loadtxt('performance_results_emrfs.txt', dtype=str)
data_hdfs = np.loadtxt('performance_results_hdfs.txt', dtype=str)

# Extract information from data for EMRFS
start_times_emrfs = data_emrfs[:, 0]
end_times_emrfs = data_emrfs[:, 1]
hyperparameters_emrfs = data_emrfs[:, 2]
fscores_emrfs = data_emrfs[:, 3].astype(float)
durations_emrfs = [(end - start).total_seconds() for start, end in zip(start_times_emrfs, end_times_emrfs)]

# Extract information from data to HDFS
start_times_hdfs = data_hdfs[:, 0]
end_times_hdfs = data_hdfs[:, 1]
hyperparameters_hdfs = data_hdfs[:, 2]
fscores_hdfs = data_hdfs[:, 3].astype(float)
durations_hdfs = [(end - start).total_seconds() for start, end in zip(start_times_hdfs, end_times_hdfs)]

# Plot F-score vs. Duration for EMRFS
plt.figure(figsize=(10, 5))
plt.scatter(durations_emrfs, fscores_emrfs, label='EMRFS', color='blue', alpha=0.5)
for i, txt in enumerate(hyperparameters_emrfs):
     plt.annotate(txt, (durations_emrfs[i], fscores_emrfs[i]))
plt.xlabel('Duration (seconds)')
plt.ylabel('F-score')
plt.title('F-score vs. Duration (EMRFS)')
plt.grid(True)
plt.legend()
plt.tight_layout()

# Plot F-score vs. Duration for HDFS
plt.figure(figsize=(10, 5))
plt.scatter(durations_hdfs, fscores_hdfs, label='HDFS', color='red', alpha=0.5)
for i, txt in enumerate(hyperparameters_hdfs):
     plt.annotate(txt, (durations_hdfs[i], fscores_hdfs[i]))
plt.xlabel('Duration (seconds)')
plt.ylabel('F-score')
plt.title('F-score vs. Duration (HDFS)')
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()