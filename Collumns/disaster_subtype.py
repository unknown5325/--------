from file_sorted import File_sort
import matplotlib.pyplot as plt

def func_disasterSubtype():
    lis = File_sort("Disaster Subtype").triage
    x_k = lis.keys()
    y_k = lis.values()
    """plt.bar(x_k, y_k, color="purple")
    plt.xticks(rotation=90)
    plt.show()"""
    print(x_k)