import numpy as np
pollution_data = np.array([[45, 65, 70], [55, 60, 50], [60, 58, 67]])

min_row = pollution_data.min(axis=1)
print(min_row)