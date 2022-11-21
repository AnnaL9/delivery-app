import csv
from Package import *
from HashTable import *

# opens the Distance CSV file
with open("CSV/Distance.csv") as distance_file:
    distance_data = csv.reader(distance_file)
    distance_data = list(distance_data)

# # opens the Packages CSV file
# with open("CSV/Packages.csv") as packages_file:
#     packages_data = csv.reader(packages_file)
#     packages_data = list(packages_data)

# opens the Addresses CSV file
with open("CSV/Addresses.csv") as Address_file:
    Address_data = csv.reader(Address_file)
    Address_data = list(Address_data)


# Reads the csv file and puts the data into the hash table by package
def load_package_data(csv_file):
    with open(csv_file) as packages:
        read_data = csv.reader(packages,
                               delimiter=',')  # reads csv data with comma as the delimiter between attributes
        package_table = HashTable()  # creates table

        # Loops through each package in the csv file by its index and assigns its attributes
        for package in read_data:
            package_ID = package[0]
            package_address = package[1]
            package_city = package[2]
            package_zip_code = package[4]
            package_deadline = package[5]
            package_weight_kilos = package[6]
            package_delivery_status = "at the hub"  # uses this status as the default status

            # creates an object for the package
            package_object = Package(package_ID, package_address, package_city, package_zip_code,
                                     package_deadline, package_weight_kilos, package_delivery_status)

            # insert the object into the hash table
            package_table.insert(package_ID, package_object)

            # # prints list of all packages in the hash table
            # HashTable.print(package_table, package_object.ID)


# passes Packages.csv file into the load_pacakge_data method
load_package_data('CSV/Packages.csv')




