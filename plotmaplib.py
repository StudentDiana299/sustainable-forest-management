import matplotlib.pyplot as plt

class DataAnalysis:
    def __init__(self, data):
        self.data = data

    def sum_of_data(self):
        # Return the sum of the data
        return sum(self.data)

    def data_doubled(self):
        # Return a new list with elements doubled
        return [2 * element for element in self.data]

    def plot_data_histogram(self):
        # Plot a histogram of the data
        plt.bar(range(len(self.data)), self.data, edgecolor='black')
        plt.title('Histogram of Data Elements')
        plt.xlabel('Index')
        plt.ylabel('Data Value')
        plt.show()

    
    # A list of annual rainfall measurements
rainfall_data = [800, 1200, 900, 1400, 1000, 1100]

# Creating an instance of DataAnalysis with rainfall data
rainfall_analysis = DataAnalysis(rainfall_data)

# Visualising the data
rainfall_analysis.plot_data_histogram()

# Accessing methods to analyse the data
total_rainfall = rainfall_analysis.sum_of_data()
rainfall_doubled = rainfall_analysis.data_doubled()
print(f'total_rainfall: {total_rainfall}')
print(f'rainfall_doubled: {rainfall_doubled}')