from LoadCSV import *

# Loads the address data from CSV
address_data = load_address_data('CSV/Addresses.csv')

# Loads the package data from CSV
package_data = load_package_data('CSV/Packages.csv')

# Loads the distance data from CSV
distance_data = load_distance_data()


# Determines the distance between the current address and the next address
# Returns float distance
def distance_between(current_address, next_address):
    distance = distance_data[next_address][current_address]
    if distance == '':
        distance = distance_data[current_address][next_address]
    return float(distance)


# Determines the address with the minimum distance from the current address
def get_closest_package(current_address, packages_in_truck):
    min_distance = None
    closest_package = None
    for package_ID in packages_in_truck.stored_keys:
        package = packages_in_truck.search(package_ID)
        package_address = package.address
        package_address_object = None
        for address in address_data:
            if address.address == package_address:
                package_address_object = address
                break
        distance = distance_between(current_address, int(package_address_object.ID))
        if min_distance is None or (distance < min_distance and distance != 0):
            min_distance = distance
            closest_package = package
    return closest_package


# Testing min distance
print(get_closest_package(1, package_data))



