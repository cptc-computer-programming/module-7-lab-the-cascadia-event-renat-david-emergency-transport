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

# Initialize lists to store route data for District 1.
dist_1_rte_time_list = []
dist_1_rte_distance_list = []
dist_1_rte_vehicles_list = []
dist_1_rte_avg_speed_list = []


# Process route data for District 1 using a for loop to iterate through the number of routes.
for i in range(1, ROUTE_COUNT + 1):
    dist_1_rte_time = int(input(f"Enter the travel time ({MIN_TRAVEL_TIME}-{MAX_TRAVEL_TIME}) for Route {i} in {district_1}: "))
    dist_1_rte_time_list.append(dist_1_rte_time)

    while dist_1_rte_time < MIN_TRAVEL_TIME or dist_1_rte_time > MAX_TRAVEL_TIME:
        print(f"Invalid input. Travel time must be between {MIN_TRAVEL_TIME} and {MAX_TRAVEL_TIME} minutes.")
        dist_1_rte_time = int(input(f"Enter the travel time ({MIN_TRAVEL_TIME}-{MAX_TRAVEL_TIME}) for Route 1 in {district_1}: "))
        dist_1_rte_time_list.append(dist_1_rte_time)

    dist_1_rte_distance = int(input(f"Enter the distance (miles) for Route {i} in {district_1}: "))
    dist_1_rte_distance_list.append(dist_1_rte_distance)

    while dist_1_rte_distance < MIN_DISTANCE:
        print(f"Invalid input. Distance must be at least {MIN_DISTANCE} miles.")
        dist_1_rte_distance = int(input(f"Enter the distance (miles) for Route {i} in {district_1}: "))
        dist_1_rte_distance_list.append(dist_1_rte_distance)

    dist_1_rte_vehicles = int(input(f"Enter the number of vehicles for Route {i} in {district_1}: "))
    dist_1_rte_vehicles_list.append(dist_1_rte_vehicles)

    while dist_1_rte_vehicles < MIN_VEHICLES:
        print(f"Invalid input. Number of vehicles must be at least {MIN_VEHICLES}.")
        dist_1_rte_vehicles = int(input(f"Enter the number of vehicles for Route {i} in {district_1}: "))
        dist_1_rte_vehicles_list.append(dist_1_rte_vehicles)
    
    dist_1_rte_avg_speed = (dist_1_rte_distance / (dist_1_rte_time / MINUTES_PER_HOUR))
    dist_1_rte_avg_speed_list.append(dist_1_rte_avg_speed)

#Calculate district-level results for District 1.
dist_1_avg_evac_time = (sum(dist_1_rte_time_list)) / ROUTE_COUNT
dist_1_avg_distance = (sum(dist_1_rte_distance_list)) / ROUTE_COUNT
dist_1_efficiency = (sum(dist_1_rte_vehicles_list)) / (sum(dist_1_rte_time_list))

# route process data for District 2
dist_2_rte_time_list = []
dist_2_rte_distance_list = []
dist_2_rte_vehicles_list = []
dist_2_rte_avg_speed_list = []

# Process route data for District 2 using a for loop to iterate through the number of routes.
for i in range(1, ROUTE_COUNT + 1):
    dist_2_rte_time = int(input(f"Enter the travel time ({MIN_TRAVEL_TIME}-{MAX_TRAVEL_TIME}) for Route {i} in {district_2}: "))
    dist_2_rte_time_list.append(dist_2_rte_time)

    while dist_2_rte_time < MIN_TRAVEL_TIME or dist_2_rte_time > MAX_TRAVEL_TIME:
        print(f"Invalid input. Travel time must be between {MIN_TRAVEL_TIME} and {MAX_TRAVEL_TIME} minutes.")
        dist_2_rte_time = int(input(f"Enter the travel time ({MIN_TRAVEL_TIME}-{MAX_TRAVEL_TIME}) for Route {i} in {district_2}: "))
        dist_2_rte_time_list.append(dist_2_rte_time)

    dist_2_rte_distance = int(input(f"Enter the distance (miles) for Route {i} in {district_2}: "))
    dist_2_rte_distance_list.append(dist_2_rte_distance)

    while dist_2_rte_distance < MIN_DISTANCE:
        print(f"Invalid input. Distance must be at least {MIN_DISTANCE} miles.")
        dist_2_rte_distance = int(input(f"Enter the distance (miles) for Route {i} in {district_2}: "))
        dist_2_rte_distance_list.append(dist_2_rte_distance)

    dist_2_rte_vehicles = int(input(f"Enter the number of vehicles for Route {i} in {district_2}: "))
    dist_2_rte_vehicles_list.append(dist_2_rte_vehicles)

    while dist_2_rte_vehicles < MIN_VEHICLES:
        print(f"Invalid input. Number of vehicles must be at least {MIN_VEHICLES}.")
        dist_2_rte_vehicles = int(input(f"Enter the number of vehicles for Route {i} in {district_2}: "))
        dist_2_rte_vehicles_list.append(dist_2_rte_vehicles)

    dist_2_rte_avg_speed = (dist_2_rte_distance / (dist_2_rte_time / MINUTES_PER_HOUR))
    dist_2_rte_avg_speed_list.append(dist_2_rte_avg_speed)

#Calculate district-level results for District 1.
dist_1_avg_evac_time = (sum(dist_1_rte_time_list)) / ROUTE_COUNT
dist_1_avg_distance = (sum(dist_1_rte_distance_list)) / ROUTE_COUNT
dist_1_efficiency = (sum(dist_1_rte_vehicles_list)) / (sum(dist_1_rte_time_list))

#Calculate district-level results for District 2.
dist_2_avg_evac_time = (sum(dist_2_rte_time_list)) / ROUTE_COUNT
dist_2_avg_distance = (sum(dist_2_rte_distance_list)) / ROUTE_COUNT
dist_2_efficiency = (sum(dist_2_rte_vehicles_list)) / (sum(dist_2_rte_time_list))

# Display route results for District 1 using a for loop to iterate through the route data lists.
for i in range(1, ROUTE_COUNT + 1):
    print(f"--- Route {i} ---")
    print(f"Travel Time: {dist_1_rte_time_list[i - 1]} minutes")
    print(f"Distance traveled: {dist_1_rte_distance_list[i - 1]} miles")
    print(f"Number of Vehicles: {dist_1_rte_vehicles_list[i - 1]}")
    print(f"Average Speed: {dist_1_rte_avg_speed_list[i - 1]:.2f} mph")
print(f"*** District 1 Summary ***")
print(f"Average Evacuation Time: {dist_1_avg_evac_time} minutes")
print(f"Average Distance: {dist_1_avg_distance} miles")
print(f"Evacuation Efficiency: {dist_1_efficiency:.2f} vehicles per minute")

# District 2 results
for i in range(1, ROUTE_COUNT + 1):
    print(f"--- Route {i} ---")
    print(f"Travel Time: {dist_2_rte_time_list[i - 1]} minutes")
    print(f"Distance traveled: {dist_2_rte_distance_list[i - 1]} miles")
    print(f"Number of Vehicles: {dist_2_rte_vehicles_list[i - 1]}")
    print(f"Average Speed: {dist_2_rte_avg_speed_list[i - 1]:.2f} mph")
print(f"*** District 2 Summary ***")
print(f"Average Evacuation Time: {dist_2_avg_evac_time} minutes")
print(f"Average Distance: {dist_2_avg_distance} miles")
print(f"Evacuation Efficiency: {dist_2_efficiency:.2f} vehicles per minute")



print("Transportation data processing complete, Thank you for using The Emergency Moon Tea Service's")