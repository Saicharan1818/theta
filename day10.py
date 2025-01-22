import matplotlib.pyplot as plt

#Sample data: a small set of values
data = [5, 7, 7, 8, 9, 10, 10, 10, 11, 12, 11, 11]

#create the histogram
plt.hist(data, bins=10, edgecolor = 'black')

plt.title('Simple Histogram Example')
plt.xlabel('Numbers')
plt.ylabel('Count')

plt.show()