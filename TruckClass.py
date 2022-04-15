class truck:
    def __init__(self, truckID, speed, time, packageList):
        self.truckID = truckID
        self.speed = speed
        self.packages = packageList
        self.time = time
        self.mileage = None
        self.location = None

    def morePackagesToDeliver(self):
        print('packages to deliver', self.numberOfPackagesToDeliver())
        for pkg in self.packages:
            if pkg.isNotDelivered():
                return True
        return False

    def deliveryComplete(self):
        return not self.morePackagesToDeliver()

    def getMileageTotal(self):
        totalMiles = 0
        for pkg in self.packages:
            totalMiles = totalMiles + pkg.mileage
        return totalMiles

    def numberOfPackagesToDeliver(self):
        counter = 0
        for pkg in self.packages:
            if pkg.isNotDelivered():
                counter += 1
        return counter
