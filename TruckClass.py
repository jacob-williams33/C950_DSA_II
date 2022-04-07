class truck:
    def __init__(self, truckID, speed, time, packageList):
        self.truckID = truckID
        self.speed = speed
        self.packages = packageList
        self.time = time
        self.mileage = None
        self.location = None

    def morePackagesToDeliver(self):
        for pkg in self.packages:
            if pkg.isNotDelivered():
                return True
        return False

    def deliveryComplete(self):
        return not self.morePackagesToDeliver()
