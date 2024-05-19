import csv
def SAN():
    with open('yyy.csv') as a:
        reader=csv.reader(a)
        for row in reader:
            print (row)
SAN()