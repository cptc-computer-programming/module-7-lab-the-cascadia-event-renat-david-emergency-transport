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


# TODO: Validate all user input.

# TODO: Calculate and display route-level and district-level results.

# TODO: Print a final completion message.