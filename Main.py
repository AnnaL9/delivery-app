import csv
from Package import *


def load_package_data(csv_file):
    with open(csv_file) as packages:
        read_data = csv.reader(packages, delimiter=',')
        next(read_data)  # skip header
        package_table = HashTable()  # create table
        for package in read_data:
            package_ID = int(package[0])
            package_address = package[1]
            package_city = package[2]
            package_state = package[3]
            package_zip_code = package[4]
            package_deadline = package[5]
            package_weight_kilos = int(package[6])

            # object
            package_test = Package(package_ID, package_address, package_city, package_state, package_zip_code,
                              package_deadline, package_weight_kilos)

            # insert it into the hash table
            package_table.insert(package_ID, package_test)

    print("Packages from Hashtable:")
    # Fetch data from Hash Table
    for i in range(len(package_table.table) + 1):
        print("Package: {}".format(package_table.search(package_test.ID)))


load_package_data('Packages.csv')
