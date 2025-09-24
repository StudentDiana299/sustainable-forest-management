import numpy as np
forest_coverage = np.array([70, 80, 65, 90, 85])
loss = 100 - forest_coverage
sum_loss = loss.sum()
total_loss_perc = sum_loss * 100

print(f"{total_loss_perc}Km squared")