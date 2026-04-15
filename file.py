import pandas as pd
import csv

files = ['1900_2021_DISASTERS.xlsx - emdat data.csv', '1970-2021_DISASTERS.xlsx - emdat data.csv']
df = pd.DataFrame()
for file in files:
    data = pd.read_csv(file)
    df = pd.concat([df, data], axis=0)
df.to_csv('merged_files.csv', index=False)


with open("merged_files.csv", "r", encoding="utf-8") as filed:
    lis = []
    csv_reader = csv.reader(filed)
    for row in csv_reader:
        lis.append(row)


for i in range(1, len(lis)):
    if lis[i-1] == lis[i]:
        lis.remove(i)


with open("merge_file.csv", "w", encoding="utf-8") as filed:
    for item in lis:
        filed.write(str(item) + '\n')