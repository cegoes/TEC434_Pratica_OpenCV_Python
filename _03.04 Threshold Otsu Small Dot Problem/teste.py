import numpy as np
a = np.array( [1, 2, 2.5, 4, 4, 6])
m = np.percentile(a, 99.7)
print(m)