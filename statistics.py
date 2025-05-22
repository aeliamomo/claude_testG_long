import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# add your list
my_list = [123, 456, 789, 234, 567, 890, 345, 678, 901, 5000, 7000, 8000]

#remove extreme values（1% ~ 99%）
lower = np.percentile(my_list, 1)
upper = np.percentile(my_list, 99)
filtered = [x for x in my_list if lower <= x <= upper]

# calculate mean, median and mode
mean_value = np.mean(filtered)
median_value = np.median(filtered)
mode_result = stats.mode(filtered, keepdims=True)
mode_value = mode_result.mode[0]

# plot the distribution of mean、median、mode
plt.figure(figsize=(10, 6))
plt.hist(filtered, bins=100, color='skyblue', edgecolor='black')


plt.axvline(mean_value, color='red', linestyle='dashed', linewidth=2, label=f'Mean = {mean_value:.2f}')
plt.axvline(median_value, color='green', linestyle='dotted', linewidth=2, label=f'Median = {median_value:.2f}')
plt.axvline(mode_value, color='blue', linestyle='solid', linewidth=2, label=f'Mode = {mode_value:.2f}')

plt.title("Distribution with Mean, Median, and Mode (Trimmed)")
plt.xlabel("Value (trimmed)")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
