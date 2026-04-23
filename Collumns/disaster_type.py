from file_sorted import File_sort
import matplotlib.pyplot as plt

def func_disasterType():
    lis = File_sort("Disaster Type").triage
    x_k = lis.keys()
    y_k = lis.values()
    explode = ()
    for i in range(0, len(x_k)):
        explode = explode + (0.1,)
    plt.pie(y_k, labels = x_k, autopct="%1.3f%%", explode=explode)
    plt.show()