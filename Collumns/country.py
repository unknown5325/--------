from file_sorted import File_sort
import matplotlib.pyplot as plt


def func_country():
    lis = File_sort("Country").triage
    x_k = lis.keys()
    y_k = lis.values()
    plt.bar(x_k, y_k, color="purple")
    plt.xticks(rotation=90)
    plt.show()

