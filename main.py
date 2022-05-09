#Jacob Williams Student ID 000680520
import csv
from Distances import distanceData
from PackageClass import package
from Addresses import addressData
from TruckClass import truck
from HashTable import ChainingHashTable
import datetime


pHash = ChainingHashTable()
#method to load packages into hash table. Time complexity of O(1)
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

#method findDistance takes a start address and determines the distance to another given address from the distance table. Time Complexity is O(1)
def findDistance(startAddress, nextAddress):

    startIndex = addressData.index(startAddress)
    nextIndex = addressData.index(nextAddress)

    if distanceData[startIndex][nextIndex] == '':
        return float(distanceData[nextIndex][startIndex])
    else:
        return float(distanceData[startIndex][nextIndex])

#loading packages from csv file
loadPackageData('Packages.csv')


#trucks are loaded manually according to constraints (packages that need to be on same truck, need early delivery, etc). Time complexity is O(N)
pkgs1 = []
pkgs1ID = [1, 2, 4, 5, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
for i in pkgs1ID:
    pkgs1.append(pHash.search(i))

truck1 = truck(1, 18, datetime.datetime(2022, 4, 7, 8), pkgs1)

pkgs2 = []
pkgs2ID = [3, 6, 18, 25, 28, 32, 36, 38]
for i in pkgs2ID:
    pkgs2.append(pHash.search(i))

truck2 = truck(1, 18, datetime.datetime(2022, 4, 7, 9, 5), pkgs2)

pkgs3 = []
pkgs3ID = [7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27, 33, 35, 39]
for i in pkgs3ID:
    pkgs3.append(pHash.search(i))

truck3 = truck(1, 18, datetime.datetime(2022, 4, 7, 10), pkgs3)

#delivery method takes the trucks and uses a nearest neighbor algorithm to determine each stop. Records delivery time, and mileage for each delivery.
#Time complexity is O(N^2)
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



#user interface
print('WGUPS Daily Local Deliveries Main Menu')
print('Deliveries began at 2022-04-07 08:00L00. Deliveries ended at: ', truck3.time)
print('Truck 1 traveled: ', truck1.getMileageTotal(), ' miles.')
print('Truck 2 traveled: ', truck2.getMileageTotal(), ' miles.')
print('Truck 3 traveled: ', truck3.getMileageTotal(), ' miles.')
print('Total Miles Driven Was: ', truck1.getMileageTotal() + truck2.getMileageTotal() + truck3.getMileageTotal(), ' miles')



#method for UI takes an input to run the program, calls printPackageStatus method to list all packages and status at any time
#Time complexity is O(N)
while True:
    try:
        runCommand = int(
            input('To Get Status of Packages at a Given Time, Enter 1 to enter new time, 0 to exit program: '))
        if runCommand == 0:
            exit()
        elif runCommand == 1:
            #continue
            hour = int(input('Enter Hour: '))
            minute = int(input('Enter Minute: '))
            if hour < 8:
                print('Deliveries Not Started')
                continue
            if hour > 24 or minute < 0 or minute > 59:
                print('Invalid Time. Re-enter')
                continue
            inputTime = datetime.datetime(2022, 4, 7, hour, minute)
            for pkgid in range(1, 41):
                pkgObject = pHash.search(pkgid)
                print(pkgObject.printPackageStatus(inputTime))

    except ValueError:
        print('Invalid Entry')
        exit()











