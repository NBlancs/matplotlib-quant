import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

fig, ax = plt.subplots()
ax.hist(data, color='red',bins=30,edgecolor='black')

ax.set_title('Random Histogram Label')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')
plt.show()
