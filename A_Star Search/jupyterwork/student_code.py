import math

def shortest_path(M,start,goal):
        
    # Create a set of discovered nodes, nodes that have not been evaluated
    discovered = set([start])
    
    # Create the set for explored nodes, nodes that have been evaluated
    explored = set([])
    
    # Dictionary to hold path distances from start to that node
    path_to_node = create_inf_dict(M.intersections)
    
    # Dictionary to hold total path distances
    path_totals = create_inf_dict(M.intersections)

    # Dictionary to map a node and the node that preceeded it to produce a path from start to end
    node_came_from = {}
    
    # Initialize the starting nodes path distance to itself, which is zero
    path_to_node[start] = 0
    
    # Initialize the starting nodes total path cost which is the distance to the goal
    path_totals[start] = heuristic(M.intersections[start], M.intersections[goal])
                      
    while (len(discovered) != 0):
        
        # Get the current node, the next node from the discovered set with the lowest total distance
        current_node = find_min_distance(discovered, path_totals)
        if (current_node == goal):            
            return (get_shortest_path(node_came_from, current_node))
        
        discovered.remove(current_node)
        explored.add(current_node)
        
        # Get a list of the neighbors of the current_node
        neighbors = M.roads[current_node]
        
        for neighbor in neighbors:
            if (neighbor in explored):
                continue
            
            if neighbor not in discovered:
                discovered.add(neighbor)
                
            temp_minimum_path = path_to_node[current_node] + dist_btwn_nodes(M.intersections[current_node], M.intersections[neighbor])
            if temp_minimum_path < path_to_node[neighbor]:
                node_came_from[neighbor] = current_node
                path_to_node[neighbor] = temp_minimum_path
                path_totals[neighbor] = path_to_node[neighbor] + heuristic(M.intersections[neighbor], M.intersections[goal])
                
    return

# Using the shortest distance dictionary and the current node, construct a list containing the shortest path
def get_shortest_path(dictionary, current_node):
    path = [current_node]    
    while (current_node in dictionary.keys()):
        current_node = dictionary[current_node]
        path.insert(0, current_node)
    return path
        
# Find the minimum distance in a dictionary by finding the min value and returning the key for that dictionary
def find_min_distance(discovered, dictionary):
    minimum = float('inf')
    key_minimum = 0
    
    for element in discovered:
        if dictionary[element] < minimum:
            minimum = dictionary[element]
            key_minimum = element
            
    return key_minimum
        
# Creates a dictionary with nodes as the keys, and infinity as the value
def create_inf_dict(intersections):
    dictionary = {}
    for entry in intersections:
        dictionary[entry] = float('inf')
    return dictionary

def heuristic(curr, goal):
    return(math.sqrt((curr[0] - goal[0])**2 + (curr[1] - goal[1])**2))

# Takes in current coordinates and the neighbor node coordinates to find the distance between
def dist_btwn_nodes(curr, neighbor):
    return(math.sqrt((curr[0] - neighbor[0])**2 + (curr[1] - neighbor[1])**2))
    
    
# Resources used to produce this code: https://en.wikipedia.org/wiki/A*_search_algorithm
        