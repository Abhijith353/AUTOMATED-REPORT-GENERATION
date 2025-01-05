import csv

# Data to be written
data = [
    ['Category', 'Value'],
    ['A', 10],
    ['B', 20],
    ['C', 30],
    ['D', 40],
    ['E', 50]
]

# Writing to csv file
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
