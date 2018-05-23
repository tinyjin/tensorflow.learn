import numpy as np
import matplotlib.pyplot as plt

# create expreiment location for 'linearRegression' #

num_points = 1000

vectors_set = []

# create location dots
for i in range(num_points) :
    x1 = np.random.normal(0.0, 0.55)
    y1 = x1 * 0.1 + 0.3 + np.random.normal(0.0, 0.03)
    vectors_set.append([x1, y1])

x_data = [v[0] for v in vectors_set]
y_data = [v[1] for v in vectors_set]

# show graph
plt.plot(x_data, y_data, 'ro')
plt.legend()
plt.show()
