import numpy as np

# Generating the random array with given size
random_array = np.random.uniform(1, 20, size=(4, 5))

random_array = np.where(random_array == random_array.max(axis=1)[:, None], 0, random_array)

print(random_array)
