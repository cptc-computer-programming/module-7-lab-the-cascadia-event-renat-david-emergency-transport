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



for district in range(1, DISTRICT_COUNT + 1):
    
    rte_time_list = []
    rte_distance_list = []
    rte_vehicles_list = []
    rte_avg_speed_list = []

    # Process route data for District 1 using a for loop to iterate through the number of routes.
    for rte in range(1, ROUTE_COUNT + 1):
        rte_time = int(input(f"Enter the travel time ({MIN_TRAVEL_TIME}-{MAX_TRAVEL_TIME}) for Route {rte} in {district_1}: "))
        rte_time_list.append(rte_time)

        while rte_time < MIN_TRAVEL_TIME or rte_time > MAX_TRAVEL_TIME:
            print(f"Invalid input. Travel time must be between {MIN_TRAVEL_TIME} and {MAX_TRAVEL_TIME} minutes.")
            rte_time = int(input(f"Enter the travel time ({MIN_TRAVEL_TIME}-{MAX_TRAVEL_TIME}) for Route {rte} in {district_1}: "))
            rte_time_list.append(rte_time)

        rte_distance = int(input(f"Enter the distance (miles) for Route {rte} in {district_1}: "))
        rte_distance_list.append(rte_distance)

        while rte_distance < MIN_DISTANCE:
            print(f"Invalid input. Distance must be at least {MIN_DISTANCE} miles.")
            rte_distance = int(input(f"Enter the distance (miles) for Route {rte} in {district_1}: "))
            rte_distance_list.append(rte_distance)

        rte_vehicles = int(input(f"Enter the number of vehicles for Route {rte} in {district_1}: "))
        rte_vehicles_list.append(rte_vehicles)

        while rte_vehicles < MIN_VEHICLES:
            print(f"Invalid input. Number of vehicles must be at least {MIN_VEHICLES}.")
            rte_vehicles = int(input(f"Enter the number of vehicles for Route {rte} in {district_1}: "))
            rte_vehicles_list.append(rte_vehicles)
        
        rte_avg_speed = (rte_distance / (rte_time / MINUTES_PER_HOUR))
        rte_avg_speed_list.append(rte_avg_speed)

    #Calculate district-level results for District 1.
    dist_1_avg_evac_time = (sum(rte_time_list)) / ROUTE_COUNT
    dist_1_avg_distance = (sum(rte_distance_list)) / ROUTE_COUNT
    dist_1_efficiency = (sum(rte_vehicles_list)) / (sum(rte_time_list))


    # Display route results for District 1 using a for loop to iterate through the route data lists.
    for i in range(1, ROUTE_COUNT + 1):
        print(f"--- Route {i} ---")
        print(f"Travel Time: {rte_time_list[i - 1]} minutes")
        print(f"Distance traveled: {rte_distance_list[i - 1]} miles")
        print(f"Number of Vehicles: {rte_vehicles_list[i - 1]}")
        print(f"Average Speed: {rte_avg_speed_list[i - 1]:.2f} mph")
    print(f"*** District {district} Summary ***")
    print(f"Average Evacuation Time: {dist_1_avg_evac_time} minutes")
    print(f"Average Distance: {dist_1_avg_distance} miles")
    print(f"Evacuation Efficiency: {dist_1_efficiency:.2f} vehicles per minute")



print("Transportation data processing complete, Thank you for using The Emergency Moon Tea Service's")