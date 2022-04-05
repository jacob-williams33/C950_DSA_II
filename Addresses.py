import csv

addressData = []

with open('addresses.csv') as fh:

    myreader = csv.reader(fh)

    for i, row in enumerate(myreader):
        addressData.append(row)

print(addressData)