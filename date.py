import csv
import matplotlib.pyplot as plt
from file_sorted import File_sort

lis = File_sort("Year").triage

y = {}

for i in lis:
    if i in y:
        y[i] += 1
    else:
        y[i] = 1



x_k = y.keys()
y_k = y.values()



plt.bar(x_k, y_k, color="purple")
plt.show()