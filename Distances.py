import csv
from Addresses import addressData
distanceData = []

with open('WGUPS Distance Table.csv') as fh:

    myreader = csv.reader(fh)

    for i, row in enumerate(myreader):
        distanceData.append(row)

print(distanceData)


def findDistance(startAddress, nextAddress):
    startIndex = []
    nextIndex = []
    for row in addressData:
        if row == startAddress:
            startIndex = addressData.index(startAddress)
    for row in addressData:
        if row == nextAddress:
            nextIndex = addressData.index(nextAddress)
    print(distanceData[startIndex][nextIndex])

# findDistance('5025 State St', '5383 S 900 East #104')
