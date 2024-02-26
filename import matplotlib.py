import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1, figsize=(7, 5))
#create a random x array of data points
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#create a random y array of data points
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filename = 'flight_distance_vs_flight_duration.png'
plt.scatter(X, y, color='blue')
plt.xlabel('Flight Distance (km)')
plt.ylabel('Flight Duration (min)')
plt.title('Flight Distance vs. Flight Duration')
plt.show()
plt.savefig(filename)
