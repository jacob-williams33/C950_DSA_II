class truck:
    def __init__(self, truckID, speed, time, packageList):
        self.truckID = truckID
        self.speed = speed
        self.packages = packageList
        self.time = time
        self.mileage = None
        self.location = None

    #determines if there are more packages to deliver
    def morePackagesToDeliver(self):

        for pkg in self.packages:
            if pkg.isNotDelivered():
                return True
        return False

    #determines if the delivery is complete
    def deliveryComplete(self):
        return not self.morePackagesToDeliver()

    #gets total mileage for the truck delivery
    def getMileageTotal(self):
        totalMiles = 0
        for pkg in self.packages:
            totalMiles = totalMiles + pkg.mileage
        return totalMiles

    #calls number of packages left to deliver if delivery is not complete
    def numberOfPackagesToDeliver(self):
        counter = 0
        for pkg in self.packages:
            if pkg.isNotDelivered():
                counter += 1
        return counter









