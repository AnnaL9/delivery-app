import csv
import datetime
from Address import *
from Package import *
from HashTable import *


# opens the Distance CSV file and loads it into a list
# Space-time complexity is O(1)
def load_distance_data():
    with open("CSV/Distance.csv", encoding='utf-8-sig') as distance_file:
        distance_data_reader = csv.reader(distance_file)
        distance_data = list(distance_data_reader)
    return distance_data


# opens the CSV file, creates an address object, and loads it into a list
# Space-time complexity is O(n)
def load_address_data(csv_file):
    address_list = list() # creates list
    with open(csv_file, encoding='utf-8-sig') as addresses:
        read_data = csv.reader(addresses, delimiter=",")
        # Loops through each address in the csv file by its index and assigns its attributes
        for address in read_data:
            address_ID = address[0]
            address_name = address[1]
            address_address = address[2]

            # creates an address object
            address_object = Address(address_ID, address_name, address_address)

            address_list.append(address_object)  # adds address object to address list

    return address_list


# Reads the csv file, creates a package object, and puts the data into the hash table by package
# Space-time complexity is O(n^3)
def load_package_data(csv_file, address_data):
    package_table = HashTable()  # creates table
    with open(csv_file) as packages:
        read_data = csv.reader(packages,
                               delimiter=',')  # reads csv data with comma as the delimiter between attributes

        # Loops through each package in the csv file by its index and assigns its attributes
        for package in read_data:
            package_ID = package[0]
            for address in address_data:
                if package[1] == address.address:
                    package_address = address
                    break
            package_city = package[2]
            package_zip_code = package[4]
            package_deadline = package[5]
            package_weight_kilos = package[6]
            package_delivery_status = "at the hub"  # uses this status as the default status
            package_delivery_time = datetime.timedelta(hours=8)

            # creates an object for the package
            package_object = Package(package_ID, package_address, package_city, package_zip_code,
                                     package_deadline, package_weight_kilos, package_delivery_status,
                                     package_delivery_time)

            # insert the object into the hash table
            package_table.insert(package_ID, package_object)

            # # prints list of all packages in the hash table
            # HashTable.print(package_table, package_object.ID)
    return package_table


