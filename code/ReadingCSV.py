#Reading CSV Dictionary As Row

import csv

with open('example.csv') as file:
    data=csv.DictReader(file)
    for row in data:
        print("SID: {} Name: {} Gender: {}".format(row["SID"],row["SNAME"],row["GENDER"]))
