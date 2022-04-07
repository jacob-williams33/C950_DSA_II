class package:
    def __init__(self, packageID, address, city, state, zip, deadline, mass):
        self.packageID = packageID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.deliveryTime = None
        self.mileage = 0

    def __str__(self):
       return "%s, %s, %s, %s, %s, %s, %s" % (self.packageID, self.address, self.city, self.state, self.zip, self.deadline,  self.mass)

    def isDelivered(self):
        return self.deliveryTime is not None

    def isNotDelivered(self):
        return not self.isDelivered()
