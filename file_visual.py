import matplotlib.pyplot as plt


class File_Vis:
    def __init__(self):
        pass

    @property
    def visual():
        explode = (0.1, 0.1, 0.1, 0.1, 0.1)
        plt.pie(y_k, labels = x_k, autopct="%1.3f%%", explode=explode)
        plt.show()


    def __del__(self):
        pass