import csv
import matplotlib.pyplot as plt
from file_sorted import File_sort


lis = File_sort("Disaster Subgroup").triage

y = {}

for i in lis:
    if i in y:
        y[i] += 1
    else:
        y[i] = 1



x_k = y.keys()
y_k = y.values()


explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
plt.pie(y_k, labels = x_k, autopct="%1.3f%%", explode=explode)
plt.show()


    


