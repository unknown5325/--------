import csv
import matplotlib.pyplot as plt
from file_sorted import File_sort


def func_date():
    lis = File_sort("Year").triage
    x_k = lis.keys()
    y_k = lis.values()
    plt.bar(x_k, y_k, color="purple")
    plt.xticks(rotation=90)
    plt.show()