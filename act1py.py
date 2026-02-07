import numpy as np
from scipy import stats

data = [95, 90, 105, 108, 105, 110, 128, 124, 108, 100, 118, 130, 120, 108, 99, 97, 106, 101, 130, 130, 91, 114, 124, 130, 112, 100, 125, 119, 126, 103, 122, 128, 124, 113, 124, 104, 94, 124, 120, 109, 126, 91, 123, 115, 111, 119, 97, 116, 106, 94, 108, 111, 104, 125, 95, 116, 99, 129, 123, 92, 126, 99, 129, 94, 118, 115, 111, 118, 125, 102, 97, 128, 94, 123, 126, 106, 96, 101, 124, 122, 100, 119, 100, 103, 110, 99, 106, 119, 93, 111, 109, 122, 118, 124, 115, 97, 110, 100, 129, 92]


print(f"Mean: {np.mean(data)}")
print(f"Median: {np.median(data)}")
print(f"Mode {stats.mode(data, keepdims=True).mode[0]}")
print(f"Range: {np.max(data) - np.min(data)}")
print(f"Variance: {np.var(data, ddof=1)}")
print(f"Standard Deviation: {np.std(data, ddof=1)}")








