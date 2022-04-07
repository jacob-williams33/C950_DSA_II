import csv
from Distances import distanceData
from PackageClass import package
from Addresses import addressData
from TruckClass import truck
from HashTable import pHash
import datetime

def findDistance(startAddress, nextAddress):

    startIndex = addressData.index(startAddress)
    nextIndex = addressData.index(nextAddress)

    if distanceData[startIndex][nextIndex] == '':
        return float(distanceData[nextIndex][startIndex])
    else:
        return float(distanceData[startIndex][nextIndex])

findDistance('HUB', '2300 Parkway Blvd')

pkgs1 = []
pkgs1ID = [1, 6, 13, 14, 15, 16, 19, 20, 25, 28, 29, 30, 32, 34, 37, 40]
for i in pkgs1ID:
    pkgs1.append(pHash.search(i))

truck1 = truck(1, 18, datetime.datetime(2022, 4, 7, 8), pkgs1)

def startDelivery(truck):
    currentAddress = 'HUB'

    while truck.morePackagesToDeliver():
        shortestMileage = 1000
        shortestPackageID = None
        for pkg in truck.packages:
            distance = findDistance(currentAddress, pkg.address)
            if distance < shortestMileage:
                shortestMileage = distance
                shortestPackageID = pkg.packageID
                pkg.mileage = distance





