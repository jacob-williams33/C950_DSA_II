import csv
from Addresses import addressData
distanceData = []

with open('WGUPS Distance Table.csv') as fh:

    myreader = csv.reader(fh)

    for i, row in enumerate(myreader):
        distanceData.append(row)

#print(distanceData)


def findDistance(startAddress, nextAddress):

    startIndex = addressData.index(startAddress)
    nextIndex = addressData.index(nextAddress)

    if distanceData[startIndex][nextIndex] == '':
        print(float(distanceData[nextIndex][startIndex]))
    else:
        print(float(distanceData[startIndex][nextIndex]))
        #return values as float - change

findDistance('HUB', '2300 Parkway Blvd')
findDistance('2300 Parkway Blvd', 'HUB')




