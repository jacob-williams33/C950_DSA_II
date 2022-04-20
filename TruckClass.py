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

    def getDeliveryTime(self):
        searchInput = input("Enter Package ID: ")
        searchID = int(searchInput)
        for pkg in self.packages:
            if searchID == pkg.packageID:
                print(pkg.mileage)
                print(pkg.deliveryTime)
                return pkg.mileage, pkg.deliveryTime

    def getPackageStatus(self):
        #searchInput = input("Enter Package ID: ")
        searchID = 1
        for pkg in self.packages:
            if searchID == pkg.packageID:
                if pkg.isDelivered:
                    print('Package has been delivered')
                elif pkg.address == 'HUB':
                    print("Package is at the hub")
                else:
                    print('Package is en route')






