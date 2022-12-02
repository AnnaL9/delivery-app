# Creates class for package
class Package:
    # Package constructor
    def __init__(self, ID, address, city, zip_code, deadline, weight_kilos, delivery_status, delivery_time):
        self.ID = ID
        self.address = address
        self.city = city
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight_kilos = weight_kilos
        self.delivery_status = delivery_status
        self.delivery_time = delivery_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.zip_code,
                                                   self.deadline, self.weight_kilos, self.delivery_status,
                                                   self.delivery_time)
