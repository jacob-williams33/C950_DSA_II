import csv
distanceData = []

with open('WGUPS Distance Table.csv') as fh:

    myreader = csv.reader(fh)

    for i, row in enumerate(myreader):
        distanceData.append(row)





