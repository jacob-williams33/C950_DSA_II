import csv
from Addresses import addressData
distanceData = []

with open('WGUPS Distance Table.csv') as fh:

    myreader = csv.reader(fh)

    for i, row in enumerate(myreader):
        distanceData.append(row)

#print(distanceData)


def findDistance(startAddress, nextAddress):
    startIndex = []
    nextIndex = []
    for row in addressData:
        if row == startAddress:
            startIndex = addressData.index(startAddress)

    for row in addressData:
        if row == nextAddress:
            nextIndex = addressData.index(nextAddress)
    if distanceData[startIndex][nextIndex] == None:
        print(distanceData[nextIndex][startIndex])
    else:
        print(distanceData[startIndex][nextIndex])
findDistance('HUB', '2300 Parkway Blvd')


