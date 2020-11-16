import csv
import numpy as np
data_ndarray = np.array([10, 20, 30])
f = open("nyc_taxis.csv", "r")
taxi_list = list(csv.reader(f))
taxi_list = taxi_list[1:]
converted_taxi_list = []

for row in taxi_list:
    converted_row = []
    for item in row:
        converted_row.append(float(item))
    converted_taxi_list.append(converted_row)

# print(converted_taxi_list)
taxi = np.array(converted_taxi_list)
taxi_shape = taxi.shape
print(taxi_shape)