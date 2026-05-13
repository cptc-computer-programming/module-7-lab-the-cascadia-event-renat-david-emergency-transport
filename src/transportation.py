# Lakewood Emergency Operations Center
# Department of Transportation

DISTRICT_COUNT = 2
ROUTE_COUNT = 3

MIN_TRAVEL_TIME = 5
MAX_TRAVEL_TIME = 300

MIN_DISTANCE = 0
MIN_VEHICLES = 1

MINUTES_PER_HOUR = 60


# TODO: Process evacuation route data for both districts.
district_1 = input("Enter the name of District 1: ")
district_2 = input("Enter the name of District 2: ")
# TODO: For each district, process all routes.

dist_1_rte_time_list = []

for i in range(1, ROUTE_COUNT + 1):
    dist_1_rte_time = int(input(f"Enter the travel time ({MIN_TRAVEL_TIME}-{MAX_TRAVEL_TIME}) for Route {i} in {district_1}: "))
    dist_1_rte_time_list.append(dist_1_rte_time)

while dist_1_rte_time < MIN_TRAVEL_TIME or dist_1_rte_time > MAX_TRAVEL_TIME:
    print(f"Invalid input. Travel time must be between {MIN_TRAVEL_TIME} and {MAX_TRAVEL_TIME} minutes.")
    dist_1_rte_time = int(input(f"Enter the travel time ({MIN_TRAVEL_TIME}-{MAX_TRAVEL_TIME}) for Route 1 in {district_1}: "))

#ROUTE 1 DATA FOR DISTRICT 1
dist_1_rte_1_time = int(input(f"Enter the travel time ({MIN_TRAVEL_TIME}-{MAX_TRAVEL_TIME}) for Route 1 in {district_1}: "))

while dist_1_rte_1_time < MIN_TRAVEL_TIME or dist_1_rte_1_time > MAX_TRAVEL_TIME:
    print(f"Invalid input. Travel time must be between {MIN_TRAVEL_TIME} and {MAX_TRAVEL_TIME} minutes.")
    dist_1_rte_1_time = int(input(f"Enter the travel time ({MIN_TRAVEL_TIME}-{MAX_TRAVEL_TIME}) for Route 1 in {district_1}: "))

dist_1_rte_1_distance = int(input(f"Enter the distance (miles) for Route 1 in {district_1}: "))

while dist_1_rte_1_distance < MIN_DISTANCE:
    print(f"Invalid input. Distance must be at least {MIN_DISTANCE} miles.")
    dist_1_rte_1_distance = int(input(f"Enter the distance (miles) for Route 1 in {district_1}: "))

dist_1_rte_1_vehicles = int(input(f"Enter the number of vehicles for Route 1 in {district_1}: "))   

while dist_1_rte_1_vehicles < MIN_VEHICLES:
    print(f"Invalid input. Number of vehicles must be at least {MIN_VEHICLES}.")
    dist_1_rte_1_vehicles = int(input(f"Enter the number of vehicles for Route 1 in {district_1}: "))

dist_1_rte_1_avg_speed = dist_1_rte_1_distance / (dist_1_rte_1_time / MINUTES_PER_HOUR)


#ROUTE 2 DATA FOR DISTRICT 1
dist_1_rte_2_time = int(input(f"Enter the travel time ({MIN_TRAVEL_TIME}-{MAX_TRAVEL_TIME}) for Route 2 in {district_1}: "))

while dist_1_rte_2_time < MIN_TRAVEL_TIME or dist_1_rte_2_time > MAX_TRAVEL_TIME:
    print(f"Invalid input. Travel time must be between {MIN_TRAVEL_TIME} and {MAX_TRAVEL_TIME} minutes.")
    dist_1_rte_2_time = int(input(f"Enter the travel time ({MIN_TRAVEL_TIME}-{MAX_TRAVEL_TIME}) for Route 2 in {district_1}: "))

dist_1_rte_2_distance = int(input(f"Enter the distance (miles) for Route 2 in {district_1}: "))

while dist_1_rte_2_distance < MIN_DISTANCE:
    print(f"Invalid input. Distance must be at least {MIN_DISTANCE} miles.")
    dist_1_rte_2_distance = int(input(f"Enter the distance (miles) for Route 2 in {district_1}: "))

dist_1_rte_2_vehicles = int(input(f"Enter the number of vehicles for Route 2 in {district_1}: "))

while dist_1_rte_2_vehicles < MIN_VEHICLES:
    print(f"Invalid input. Number of vehicles must be at least {MIN_VEHICLES}.")
    dist_1_rte_2_vehicles = int(input(f"Enter the number of vehicles for Route 2 in {district_1}: "))

dist_1_rte_2_avg_speed = dist_1_rte_2_distance / (dist_1_rte_2_time / MINUTES_PER_HOUR)

#ROUTE 3 DATA FOR DISTRICT 1
dist_1_rte_3_time = int(input(f"Enter the travel time ({MIN_TRAVEL_TIME}-{MAX_TRAVEL_TIME}) for Route 3 in {district_1}: "))

while dist_1_rte_3_time < MIN_TRAVEL_TIME or dist_1_rte_3_time > MAX_TRAVEL_TIME:
    print(f"Invalid input. Travel time must be between {MIN_TRAVEL_TIME} and {MAX_TRAVEL_TIME} minutes.")
    dist_1_rte_3_time = int(input(f"Enter the travel time ({MIN_TRAVEL_TIME}-{MAX_TRAVEL_TIME}) for Route 3 in {district_1}: "))

dist_1_rte_3_distance = int(input(f"Enter the distance (miles) for Route 3 in {district_1}: "))

while dist_1_rte_3_distance < MIN_DISTANCE:
    print(f"Invalid input. Distance must be at least {MIN_DISTANCE} miles.")
    dist_1_rte_3_distance = int(input(f"Enter the distance (miles) for Route 3 in {district_1}: "))

dist_1_rte_3_vehicles = int(input(f"Enter the number of vehicles for Route 3 in {district_1}: "))

while dist_1_rte_3_vehicles < MIN_VEHICLES:
    print(f"Invalid input. Number of vehicles must be at least {MIN_VEHICLES}.")
    dist_1_rte_3_vehicles = int(input(f"Enter the number of vehicles for Route 3 in {district_1}: "))

dist_1_rte_3_avg_speed = dist_1_rte_3_distance / (dist_1_rte_3_time / MINUTES_PER_HOUR)

#misc data (temporary)
dist_1_avg_evac_time = (dist_1_rte_1_time + dist_1_rte_2_time + dist_1_rte_3_time) / ROUTE_COUNT
dist_1_avg_distance = (dist_1_rte_1_distance + dist_1_rte_2_distance + dist_1_rte_3_distance) / ROUTE_COUNT
dist_1_efficiency = (dist_1_rte_1_vehicles + dist_1_rte_2_vehicles + dist_1_rte_3_vehicles) / (dist_1_rte_1_time + dist_1_rte_2_time + dist_1_rte_3_time)



# TODO: Calculate and display route-level and district-level results.
print(f"*** District 1: {district_1} ***")
print("--- Route 1 ---")
print(f"Travel Time: {dist_1_rte_1_time} minutes")
print(f"Distance traveled: {dist_1_rte_1_distance} miles")
print(f"Number of Vehicles: {dist_1_rte_1_vehicles}")
print(f"Average Speed: {dist_1_rte_1_avg_speed:.2f} mph")
print("--- Route 2 ---")
print(f"Travel Time: {dist_1_rte_2_time} minutes")
print(f"Distance traveled: {dist_1_rte_2_distance} miles")
print(f"Number of Vehicles: {dist_1_rte_2_vehicles}")
print(f"Average Speed: {dist_1_rte_2_avg_speed:.2f} mph")
print("--- Route 3 ---")
print(f"Travel Time: {dist_1_rte_3_time} minutes")
print(f"Distance traveled: {dist_1_rte_3_distance} miles")
print(f"Number of Vehicles: {dist_1_rte_3_vehicles}")
print(f"Average Speed: {dist_1_rte_3_avg_speed:.2f} mph")
print(f"*** District 1 Summary ***")
print(f"Average Evacuation Time: {dist_1_avg_evac_time} minutes")
print(f"Average Distance: {dist_1_avg_distance} miles")
print(f"Evacuation Efficiency: {dist_1_efficiency} vehicles per minute")

# district 2
print(f"*** District 2: {district_2} ***")
print("--- Route 1 ---")
print(f"Travel Time: {dist_2_rte_1_time} minutes")
print(f"Distance traveled: {dist_2_rte_1_distance} miles")
print(f"Number of Vehicles: {dist_2_rte_1_vehicles}")
print(f"Average Speed: {dist_2_rte_1_avg_speed:.2f} mph")
print("--- Route 2 ---")
print(f"Travel Time: {dist_2_rte_2_time} minutes")
print(f"Distance traveled: {dist_2_rte_2_distance} miles")
print(f"Number of Vehicles: {dist_2_rte_2_vehicles}")
print(f"Average Speed: {dist_2_rte_2_avg_speed:.2f} mph")
print("--- Route 3 ---")
print(f"Travel Time: {dist_2_rte_3_time} minutes")
print(f"Distance traveled: {dist_2_rte_3_distance} miles")
print(f"Number of Vehicles: {dist_2_rte_3_vehicles}")
print(f"Average Speed: {dist_2_rte_3_avg_speed:.2f} mph")
print(f"*** District 2 Summary ***")
print(f"Average Evacuation Time: {dist_2_avg_evac_time} minutes")
print(f"Average Distance: {dist_2_avg_distance} miles")
print(f"Evacuation Efficiency: {dist_2_efficiency} vehicles per minute")
# TODO: Print a final completion message.
print("Transportation data processing complete, Thank you for using The Emergency Moon Tea Service's")