# Creates class for truck
class Truck:
    def __init__(self, capacity, speed, packages, mileage, address, depart_time, current_time):
        self.capacity = capacity
        self.speed = speed
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time
        self.current_time = current_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.capacity, self.speed, self.packages, self.mileage,
                                               self.address, self.depart_time, self.current_time)
