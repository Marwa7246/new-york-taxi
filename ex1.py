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

print(converted_taxi_list)
taxi = np.array(converted_taxi_list)
taxi_shape = taxi.shape
print(taxi)

row_0 = taxi[0]
rows_1_to_3 = taxi[1:4]
row_21_column_5 = taxi[1,5]

cols = [1,4,7]
columns_1_4_7 = taxi[:,cols]
row_99_columns_5_to_8 =taxi[99, 5:9]
rows_100_to_200_column_14 = taxi[100:201, 14]

print(rows_1_to_3)

cols = [1,4,7]
columns_1_4_7 = taxi[:,cols]
row_99_columns_5_to_8 =taxi[99, 5:9]
rows_100_to_200_column_14 = taxi[100:201, 14]

fare_amount = taxi[:,9]
fees_amount = taxi[:,10]
fare_and_fees = fare_amount + fees_amount
