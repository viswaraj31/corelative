import csv
import numpy as n

list1 = []
list2 = []

with open("tv.csv",newline="") as f :
    r = csv.DictReader(f)

    for i in r :
        list1.append(float(i["Coffee in ml"]))
        list2.append(float(i["sleep in hours"]))

datasource = {'x':list1,'y':list2}

corr = n.corrcoef(datasource["x"],datasource["y"])

print(corr[0,1])