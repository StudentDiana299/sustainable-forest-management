import numpy as np
water_quality = np.array([[7.8, 6.5, 8.0], [5.4, 7.2, 6.5]])
worst_avg_q_parameter = water_quality.min(axis=1)
print(worst_avg_q_parameter)

animal_sightings = np.array([[5, 7, 8], [3, 4, 6], [9, 10, 7]])
high_avg_sightings = animal_sightings.max()
print(high_avg_sightings)

bird_sightings = np.array([3, 4, 2, 5, 1, 0, 4, 3, 5, 2, 1, 7, 8, 1, 2, 3, 4, 1, 0, 5, 6, 2, 3, 4, 1, 4, 6, 7])
shapings = bird_sightings.reshape(4,7)
total_sightings_per_week = shapings.sum(axis=1)
print(total_sightings_per_week)

climate_data = np.array([[22, 50], [25, 43], [28, 35], [30, 20], [27, 25], [25, 30], [23, 40], [24, 55], [22, 60], [20, 65], [18, 70], [22, 58]])
Trans = climate_data.transpose()
print(Trans)