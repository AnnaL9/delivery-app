# Creates class for address
class Address:
    # Address constructor
    def __init__(self, ID, name, address):
        self.ID = ID
        self.name = name
        self.address = address

    def __str__(self):
        return "%s, %s, %s" % (self.ID, self.name, self.address)
