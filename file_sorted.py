import csv
from collections import Counter


class File_sort:
    def __init__(self, collumn):
        self.coll = collumn


    @property
    def triage(self):
        with open("1900_2021_DISASTERS.xlsx - emdat data.csv", "r", encoding="utf-8") as file_dis:
            csv_reader = csv.DictReader(file_dis)
            lis = []
            for row in csv_reader:
                lis.append(row[self.coll])

        for i in range(0,len(lis)-1): #Цикл для всех элементов списка
            for k in range(0,len(lis)-1 - i): #Начинаем проверку элементов
                if lis[k] > lis[k+1]:  #В порядке убывания
                    lis[k], lis[k+1] = lis[k+1], lis[k] #Меняем элементы местами

        lis = Counter(lis)
        return lis


    def __del__(self):
        pass