import csv
from Distances import distanceData
from PackageClass import package
from Addresses import addressData
from TruckClass import truck
from HashTable import ChainingHashTable
import datetime


pHash = ChainingHashTable()

def loadPackageData(fileName):
    with open(fileName) as packages:
        packageData = csv.reader(packages, delimiter=',')
        for pack in packageData:
            pID = int(pack[0])
            address = pack[1]
            city = pack[2]
            state = pack[3]
            zip = pack[4]
            deadline = pack[5]
            mass = pack[6]


            # package object
            p = package(pID, address, city, state, zip, deadline, mass)
            # print(p)

            # insert it into the hash table
            pHash.insert(pID, p)


def findDistance(startAddress, nextAddress):

    startIndex = addressData.index(startAddress)
    nextIndex = addressData.index(nextAddress)

    if distanceData[startIndex][nextIndex] == '':
        return float(distanceData[nextIndex][startIndex])
    else:
        return float(distanceData[startIndex][nextIndex])

loadPackageData('Packages.csv')

pkgs1 = []
pkgs1ID = [1, 6, 13, 14, 15, 16, 19, 20, 25, 28, 29, 30, 32, 34, 37, 40]
for i in pkgs1ID:
    pkgs1.append(pHash.search(i))

truck1 = truck(1, 18, datetime.datetime(2022, 4, 7, 8), pkgs1)


def startDelivery(truck):
    currentAddress = 'HUB'
    currentTime = datetime.datetime(2022, 4, 7, 8)

    while truck.morePackagesToDeliver():

        shortestMileage = 1000
        shortestPackage = None


        for pkg in truck.packages:
            if pkg.isNotDelivered():
                distance = findDistance(currentAddress, pkg.address)
                if distance < shortestMileage:
                    shortestMileage = distance
                    shortestPackage = pkg
                    timeToDeliver = shortestMileage / 18
                    time_obj = datetime.timedelta(hours=timeToDeliver)


        shortestPackage.deliveryTime = currentTime + time_obj
        currentTime = shortestPackage.deliveryTime
        print(shortestPackage.deliveryTime)
        shortestPackage.mileage = shortestMileage
        currentAddress = shortestPackage.address


    print(truck.getMileageTotal())
    print(shortestPackage.deliveryTime)

startDelivery(truck1)
truck1.getDeliveryTime()
truck1.getPackageStatus()







