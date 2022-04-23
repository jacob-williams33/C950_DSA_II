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

pkgs2 = []
pkgs2ID = [2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 17, 18, 21, 22, 23, 24]
for i in pkgs2ID:
    pkgs2.append(pHash.search(i))

truck2 = truck(1, 18, datetime.datetime(2022, 4, 7, 8), pkgs2)

pkgs3 = []
pkgs3ID = [25, 26, 27, 31, 33, 35, 36, 38, 39]
for i in pkgs3ID:
    pkgs3.append(pHash.search(i))

truck3 = truck(1, 18, datetime.datetime(2022, 4, 7, 10), pkgs3)


def startDelivery(truck):
    currentAddress = 'HUB'
    currentTime = truck.time
    shortestPackage = None

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


        currentTime = currentTime + time_obj
        shortestPackage.deliveryTime = currentTime

        shortestPackage.mileage = shortestMileage
        currentAddress = shortestPackage.address

    returnTrip = findDistance(shortestPackage.address,'HUB')
    endTripMiles = truck.getMileageTotal() + returnTrip
    endTripTime = truck.time + datetime.timedelta(hours=endTripMiles/18)
    truck.time = endTripTime


startDelivery(truck1)
startDelivery(truck2)
startDelivery(truck3)


print('WGUPS Daily Local Deliveries Main Menu')
print('Deliveries began at 2022-04-07 08:00L00. Deliveries ended at: ', truck3.time)
print('Total Miles Driven Was: ', truck1.getMileageTotal() + truck2.getMileageTotal() + truck3.getMileageTotal())

while True:
    try:
        runCommand = int(
            input('To Get Status of Packages at a Given Time, Enter 1 to enter new time, 0 to exit program: '))
        if runCommand == 0:
            exit()
        elif runCommand == 1:
            #continue
            hour = int(input('Enter Hour as HH: '))
            minute = int(input('Enter Minute as MM: '))
            if hour < 8:
                print('Deliveries Not Started')
                continue
            if hour > 24 or minute < 0 or minute > 59:
                print('Invalid Time. Re-enter')
                continue
            inputTime = datetime.datetime(2022, 4, 7, hour, minute)
            for pkgid in range(1, 40):
                pkgObject = pHash.search(pkgid)
                print(pkgObject.printPackageStatus(inputTime))

    except ValueError:
        print('Invalid Entry')
        exit()









