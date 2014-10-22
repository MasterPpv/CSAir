'''
@author: Priten Vora
'''
from Graph import Graph
from Node import Node
from decimal import Decimal
from decimal import getcontext
import webbrowser
getcontext().prec = 8
import json
import sys

def create_graph_nodes(map_data, my_graph):
    '''
    Takes JSON data and a Graph object and creates
    new, as-yet unconnected nodes in the graph in
    order to have nodes to add edges to and from
    '''
    for city in map_data["metros"]:
        new_node = Node(city)
        my_graph.add_node(new_node)

def create_graph_edges(map_data, my_graph):
    '''
    Takes JSON data and a Graph object with some
    previously created, but as-yet unconnected,
    nodes in it and creates edges throughout the
    graph to connect the nodes according to the
    JSON data, along with giving each edge some
    weight, also according to the same JSON data
    '''
    for route in map_data["routes"]:
        port1 = route["ports"][0]
        port2 = route["ports"][1]
        route_distance = Decimal(route["distance"])
        graph_nodes = my_graph.get_nodes()
        node_vertices = []
        for current_node in graph_nodes:
            node_data = current_node.get_data()
            if node_data["code"] == port1 or node_data["code"] == port2:
                node_vertices.append(current_node)
        vertices = tuple(node_vertices)
        my_graph.add_edge(vertices, route_distance)

def read_json(file_name):
    '''
    A simple JSON file reader that reads from a given filename
    (which should be a JSON file) and returns all of the JSON
    data from that file.
    '''
    file_descriptor = open(file_name)
    json_data = json.load(file_descriptor)
    file_descriptor.close()
    return json_data

def interpret_response(user_response):
    '''
    Very basic interpreter for what the user inputs in the main
    menu. Takes in their input and returns an integer corresponding
    to the appropriate option based on their selection. Returns
    a value of -1 if the input did not match any of the menu items. 
    '''
    if user_response == "1":
        return 1
    elif user_response == "2":
        return 2
    elif user_response == "3":
        return 3
    elif user_response == "4":
        return 4
    elif user_response == "5":
        return 5
    else:
        return -1

def print_all_cities(my_graph):
    '''
    Traverses through the graph city by city and prints
    out a list of all the cities in the route network,
    along with their graph.
    '''
    all_nodes = my_graph.get_nodes()
    output_string = "\nThese are all of the cities that CSAir serves:"
    first_city = True
    for current_node in all_nodes:
        node_data = current_node.get_data()
        city_name = str(node_data["name"])
        city_code = str(node_data["code"])
        if first_city:
            output_string += " " + city_name + " (" + city_code + ")"
            first_city = False
        else:
            output_string += ", " + city_name + " (" + city_code + ")"
    output_string += ".\n"
    print output_string

def print_single_city(city):
    '''
    Prints out all relevant data for a single city,
    including its name, airport code, country, time
    zone, continent, global coordinates in terms of
    latitude and longitude, population, and region.
    Also prints out a list of all other cities that
    this city has outgoing flights to, and also the
    distance of the flight (in kilometers and miles)
    '''
    # Print out all the basic, easy-to-get values
    city_data = city.get_data()
    print "Code:", city_data["code"]
    print "Name:", city_data["name"]
    print "Country:", city_data["country"]
    print "Continent:", city_data["continent"]
    print "Timezone:", city_data["timezone"]
    city_coordinates = city_data["coordinates"]
    coordinate_keys = city_coordinates.keys()
    coordinate_values = city_coordinates.values()
    print "Latitude:", coordinate_values[0], coordinate_keys[0]
    print "Longitude:", coordinate_values[1], coordinate_keys[1]
    print "Population:", city_data["population"]
    print "Region:", city_data["region"]

    # Find out what cities this city has outgoing flights to
    destinations = city.get_neighbors_out()
    routes_out = city.get_routes_out()
    print "Has outgoing flights to the following:"
    counter = 0
    for destination in destinations:
        destination_data = destination.get_data()
        destination_code = destination_data["code"]
        destination_name = destination_data["name"]
        route_distance_km = routes_out[counter].get_weight()
        counter += 1
        route_distance_mi = route_distance_km * Decimal(0.621371)
        print "------------------------------------------------------------"
        print "Destination:", destination_name, "(%s)" %destination_code
        print "Flight distance:", route_distance_km, "km /", route_distance_mi, "mi"

def handle_city_query(my_graph):
    '''
    Handles everything that happens when the user opts
    from the main menu to gather information about one
    city. Queries the user about what city they want to
    get information about, accepting either the name or
    the airport code of the city to identify it. Makes
    sure that the user provides valid input, but allows
    the user to back out into the main menu if they so
    choose. If the user enters an acceptable city code
    or name, that city's data is printed out.
    '''
    # Set up needed variables
    all_nodes = my_graph.get_nodes()
    all_codes = []
    all_names = []
    for current_node in all_nodes:
        node_data = current_node.get_data()
        all_codes.append(str(node_data["code"]).lower())
        all_names.append(str(node_data["name"]).lower())
    keep_trying = True

    # Query user to find out which city's data they want
    while keep_trying:
        print "Enter either the name or the code of the city you want info about:"
        response = raw_input().lower()

        # Check if the user entered a code to identify the city
        if response in all_codes:
            code_index = all_codes.index(response)
            found_city = all_nodes[code_index]
            print
            print_single_city(found_city)
            print
            keep_trying = False

        # Check if the user entered a name to identify the city
        elif response in all_names:
            name_index = all_names.index(response)
            found_city = all_nodes[name_index]
            print
            print_single_city(found_city)
            print
            keep_trying = False

        # Handle invalid input and ask user whether to try again or go back
        else:
            print "This is not the name or code of a city in our network. Try again? (y or n)"
            trying = raw_input()
            while trying.lower() != "y" and trying.lower() != "n":
                print "Invalid input. Keep trying? (y or n)"
                trying = raw_input()
            if trying.lower() == "n":
                keep_trying = False

def print_longest_flight(my_graph):
    '''
    Prints out data about the longest single flight in the
    route network, including the names and codes of the
    starting and ending cities, and the flight distance of
    said flight in both kilometers and meters.
    '''
    flight = my_graph.get_longest_edge()
    flight_endpoints = flight.get_endpoints()
    flight_start = flight_endpoints[0]
    flight_start_data = flight_start.get_data()
    flight_end = flight_endpoints[1]
    flight_end_data = flight_end.get_data()
    flight_km = flight.get_weight()
    flight_mi = flight_km * Decimal(0.621371)
    print "Longest single flight:", flight_start_data["name"], "(%s) to"\
    %flight_start_data["code"], flight_end_data["name"], "(%s)" %flight_end_data["code"]
    print "Longest flight distance:", flight_km, "km /", flight_mi, "mi"

def print_shortest_flight(my_graph):
    '''
    Prints out data about the shortest single flight in the
    route network, including the names and codes of the
    starting and ending cities, and the flight distance of
    said flight in both kilometers and meters.
    '''
    flight = my_graph.get_shortest_edge()
    flight_endpoints = flight.get_endpoints()
    flight_start = flight_endpoints[0]
    flight_start_data = flight_start.get_data()
    flight_end = flight_endpoints[1]
    flight_end_data = flight_end.get_data()
    flight_km = flight.get_weight()
    flight_mi = flight_km * Decimal(0.621371)
    print "Shortest single flight:", flight_start_data["name"], "(%s) to"\
    %flight_start_data["code"], flight_end_data["name"], "(%s)" %flight_end_data["code"]
    print "Shortest flight distance:", flight_km, "km /", flight_mi, "mi"

def print_average_flight_distance(my_graph):
    '''
    Prints out the average flight distance in both kilometers
    and meters across all flights in the route network.
    '''
    average_flight_km = my_graph.get_average_edge_weight()
    average_flight_mi = average_flight_km * Decimal(0.621371)
    print "Average flight distance:", average_flight_km, "km /", average_flight_mi, "mi"

def print_cities_by_population(my_graph):
    '''
    Calculates and prints out which city in the route network
    has the lowest and highest populations, along with those
    cities' names and codes. Also calculates and prints out
    the average population across all cities in the network.
    '''
    # Setting up the variables
    all_nodes = my_graph.get_nodes()
    all_populations = []
    for current_node in all_nodes:
        node_data = current_node.get_data()
        all_populations.append(node_data["population"])
    sorted_populations = all_populations[:]
    sorted_populations.sort()

    # Grabbing the actual smallest and largest values
    smallest_population = sorted_populations[0]
    largest_population = sorted_populations[len(sorted_populations) - 1]

    # Smallest population stuff
    smallest_city_index = all_populations.index(smallest_population)
    smallest_city = all_nodes[smallest_city_index]
    smallest_city_data = smallest_city.get_data()
    print "Least populated city:", smallest_city_data["name"], "(%s)" %smallest_city_data["code"]
    print "Smallest population:", smallest_population
    print "------------------------------------------------------------"

    # Largest population stuff
    largest_city_index = all_populations.index(largest_population)
    largest_city = all_nodes[largest_city_index]
    largest_city_data = largest_city.get_data()
    print "Most populated city:", largest_city_data["name"], "(%s)" %largest_city_data["code"]
    print "Largest population:", largest_population
    print "------------------------------------------------------------"

    # Average population stuff
    num_cities = Decimal(len(my_graph.get_nodes()))
    sum_population = Decimal(0)
    for city_population in all_populations:
        sum_population += city_population
    average = Decimal(sum_population / num_cities)
    print "Average population:", average

def print_continents(my_graph):
    '''
    Prints out a list of the continents served by the CSAir
    route network, as well as which cities in each of those
    continents have airports serviced by CSAir.
    '''
    # Set up a dictionary of all continents and their respective cities
    all_nodes = my_graph.get_nodes()
    all_continents = {}
    for current_node in all_nodes:
        node_data = current_node.get_data()
        current_continent = str(node_data["continent"])
        if current_continent not in all_continents:
            all_continents[current_continent] = []
        all_continents[current_continent].append(current_node)

    # In case user has removed all cities from the route network
    if len(all_continents) <= 0:
        print "There are no continents currently in CSAir's route network."
        return

    # Print out each continent one by one
    for continent in all_continents:

        # Set up variables
        city_list = all_continents[continent]
        continent_output = ""
        if len(city_list) > 0:
            continent_output = "All cities in " + continent + ":"

        # In case user has removed all cities in this continent
        else:
            continent_output = "There are no cities in " + continent + "."
            print continent_output
            continue

        # Append each city's information to the output string
        first_city = True
        for current_city in city_list:
            city_data = current_city.get_data()
            city_name = str(city_data["name"])
            city_code = str(city_data["code"])
            if first_city:
                continent_output += " " + city_name + " (" + city_code + ")"
                first_city = False
            else:
                continent_output += ", " + city_name + " (" + city_code + ")"

        # Format and print output
        continent_output += "."
        print continent_output

def print_hub_cities(my_graph):
    '''
    Prints out a list of all of the hub cities in the
    CSAir route network, as well as the number of direct
    connections they have to other cities in the network.
    '''
    # Get the graph's hub list
    hub_list = my_graph.get_hub_list()

    # In case there aren't any hubs
    if len(hub_list) <= 0:
        print "There are no hub cities in the network"

    # In case there's only one hub
    elif len(hub_list) == 1:
        hub_city = hub_list[0]
        hub_data = hub_city.get_data()
        hub_degree = hub_city.get_degree()
        print "Hub city: ", hub_data["name"], "(%s)" %hub_data["code"],\
        "with ", hub_degree, "unique connections."

    # In case there are multiple hubs
    else:
        hub_output = "Hub cities:"
        first_city = True

        # Add each hub city to the output string
        for hub_city in hub_list:
            hub_data = hub_city.get_data()
            hub_name = str(hub_data["name"])
            hub_code = str(hub_data["code"])
            hub_degree = hub_city.get_degree()
            if first_city:
                hub_output += " " + hub_name + " (" + hub_code + ") "\
                + "with " + str(hub_degree) + " unique connections"
                first_city = False
            else:
                hub_output += ", " + hub_name + " (" + hub_code + ") "\
                + "with " + str(hub_degree) + " unique connections"

        # Format and print output
        hub_output += "."
        print hub_output

def handle_stats_query(my_graph):
    '''
    Handles everything that happens when the user opts
    from the main menu to gather information about the
    route network in general. Prints information about
    the longest and shortest flights in the network,
    the average flight distance across all flights in
    the network, the cities with the smallest and the
    largest population that are served by the network,
    and the average population of all cities served.
    Also prints a list of all the continents served by
    CSAir and which cities in each of those continents
    have airports that CSAir services. Finally, prints
    a list of the hub cities in the route network, as
    well as the number of direct connections that each
    one has to the other cities in the network.
    '''
    print
    print_longest_flight(my_graph)
    print "------------------------------------------------------------"
    print_shortest_flight(my_graph)
    print "------------------------------------------------------------"
    print_average_flight_distance(my_graph)
    print "------------------------------------------------------------"
    print_cities_by_population(my_graph)
    print "------------------------------------------------------------"
    print_continents(my_graph)
    print "------------------------------------------------------------"
    print_hub_cities(my_graph)
    print

def visulaize_map(my_graph):
    '''
    '''
    print "Opening map in browser..."
    result_url = "http://www.gcmap.com/mapui?P="
    all_nodes = my_graph.get_nodes()
    all_edges = my_graph.get_edges()
    for current_node in all_nodes:
        current_in_routes = current_node.get_routes_in()
        current_out_routes = current_node.get_routes_out()
        node_data = current_node.get_data()
        if current_in_routes == [] and current_out_routes == []:
            result_url += str(node_data["code"]) + ","
    for current_edge in all_edges:
        current_start, current_end = current_edge.get_endpoints()
        start_data = current_start.get_data()
        end_data = current_end.get_data()
        result_url += str(start_data["code"]) + "-" + str(end_data["code"]) + ","
    webbrowser.open_new(result_url)
    print "Done!"

def main():

    # Reads map data JSON file and populates a Graph object with the data
    my_graph = Graph()
    map_data = read_json("map_data.json")
    create_graph_nodes(map_data, my_graph)
    create_graph_edges(map_data, my_graph)

    # Keep allowing user to perform tasks until they choose to exit
    keep_running = True
    while keep_running:
        print "Welcome to CSAir! What would you like to do?"
        print "(1) List cities (2) Get info about a city (3) Get network stats (4) View Map (5) Exit"

        # Using raw_input instead of input because it reads things in as strings
        response = raw_input()
        interpreted = interpret_response(response)

        # Handle case where user entered invalid input
        while interpreted == -1:
            print "Invalid input. Please try again (choose a number from the following):"
            print "(1) List all cities (2) Get info about a city (3) Get network stats (4) View map (5) Exit"
            response = raw_input()
            interpreted = interpret_response(response)

        # Handle case where user decided to exit
        if interpreted == 5:
            print "Thank you for using CSAir!"
            keep_running = False

        # Handle case where user decided to get a list printed of all the cities
        elif interpreted == 1:
            print_all_cities(my_graph)

        # Handle case where user wants to get info about a specific city
        elif interpreted == 2:
            handle_city_query(my_graph)

        # Handle case where user wants to get network stats
        elif interpreted == 3:
            handle_stats_query(my_graph)

        elif interpreted == 4:
            visulaize_map(my_graph)

        # Handle case where the interpreter let input through but it was wrong
        else:
            print "Something about the input messed everything up! Oh no!"
            sys.exit(1)

if __name__ == '__main__':
    main()