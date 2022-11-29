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
def min_distance_from(current_address, packages):
    min_distance = None
    for package in packages:
        distance = distance_between(current_address, int(package[0]))
        if min_distance is None or (distance < min_distance and distance != 0):
            min_distance = distance
    return min_distance



