import datetime

from LoadCSV import *
from Truck import *

# Loads the address data from CSV
address_data = load_address_data('CSV/Addresses.csv')

# Loads the package data from CSV
package_data = load_package_data('CSV/Packages.csv', address_data)

# Loads the distance data from CSV
distance_data = load_distance_data()

# Initiates Truck 1 object
truck1 = Truck(16, 18.0, [], 0.0, address_data[0],
               datetime.timedelta(hours=8), datetime.timedelta(hours=8))

# Initiates Truck 2 object
truck2 = Truck(16, 18.0, [], 0.0, address_data[0],
               datetime.timedelta(hours=8), datetime.timedelta(hours=8))

# Initiates Truck 3 object
truck3 = Truck(16, 18.0, [], 0.0, address_data[0],
               datetime.timedelta(hours=10, minutes=20), datetime.timedelta(hours=10, minutes=20))


# Loads the truck with list of package objects
def load_truck(truck, list_of_packages):
    for x in list_of_packages:
        package = package_data.search(x)
        truck.packages.append(package)
        packages_at_hub.remove(x)


packages_at_hub = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                   '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35',
                   '36', '37', '38', '39', '40']
# Loads trucks with specified packages
load_truck(truck1, ['1', '2', '4', '5', '7', '8', '10', '11', '12', '13', '14', '15', '16', '19', '20'])
load_truck(truck2, ['3', '17', '18', '21', '22', '23', '24', '25', '27', '29', '30', '31', '33', '34', '36', '38'])
load_truck(truck3, ['6', '26', '28', '32', '9', '35', '37', '39', '40'])
# print(packages_at_hub)


# Determines if there is a time conflict with delivering certain packages
def package_time_conflict(current_package, truck):
    # package = truck.packages.search(package_ID)
    if (truck.current_time < datetime.timedelta(hours=10, minutes=20)) and \
            (current_package.ID == '9'):
        return True
    else:
        return False


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
    closest_package_address = None
    current_address_ID = current_address.ID
    for package in packages_in_truck:
        package_address = package.address.address
        package_address_object = None
        for address in address_data:
            if address.address == package_address:
                package_address_object = address
                break
        distance = distance_between(int(current_address_ID), int(package_address_object.ID))
        if min_distance is None or (distance < min_distance and distance != 0.0):
            min_distance = distance
            closest_package_address = package.address
    return closest_package_address


# # Testing min distance
# print(get_closest_package(1, package_data))


# Delivers the packages on the truck
def deliver_packages(truck, all_packages):
    current_address = truck.address
    not_delivered = truck.packages

    for current_package in not_delivered:
        if package_time_conflict(current_package, truck) is False:
            current_package.delivery_status = "en route"  # sets each package delivery status to "en route"
            package_address = current_package.address
            # calls the get_closest_package function and assigns value to next_delivery
            next_delivery = get_closest_package(package_address, truck.packages)

            # Calculates delivery time
            distance = distance_between(int(current_address.ID), int(next_delivery.ID))
            truck.mileage += distance  # adds the distance traveled to the truck mileage
            speed = truck.speed
            time_to_deliver = datetime.timedelta(hours=(distance / speed))  # Calculates time it took to deliver

            # Updates times
            current_time = truck.current_time + time_to_deliver
            truck.current_time = current_time
            current_package.delivery_time = current_time

            # Updates addresses
            current_address = next_delivery
            truck.address = next_delivery  # assigns the truck address to the next delivery address

            # Marks package delivery status as delivered
            current_package.delivery_status = "delivered"

            # Removes package from not delivered list
            not_delivered.remove(current_package)


# deliver truck 1 package
deliver_packages(truck1, package_data)
deliver_packages(truck2, package_data)
deliver_packages(truck3, package_data)

total_mileage = truck1.mileage + truck2.mileage + truck3.mileage
print(truck1.mileage, '+', truck2.mileage, '+', truck3.mileage, "=", total_mileage)
# print(truck1)
# print(truck1.packages[0])
