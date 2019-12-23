from math import sqrt, ceil, floor

def spiral_level_for_memory_location(location):
    return ceil((sqrt(location) - 1) / 2)

target_memory_location = 289326

spiral_level = spiral_level_for_memory_location(target_memory_location)
spiral_edge_size = 2 * spiral_level + 1
spiral_level_max_location = spiral_edge_size ** 2

distance_from_max_location = spiral_level_max_location - target_memory_location
distance_from_edge_corner = distance_from_max_location % (spiral_edge_size - 1)
distance_from_edge_center = abs(floor(spiral_edge_size / 2) - distance_from_edge_corner)
distance_to_access_port = distance_from_edge_center + spiral_level

print("Distance to access port is: {}".format(distance_to_access_port))

# Second part is messy, but so is the assignment, could not bear to make dynamic 2D array (or make
# a huge empty array to fit the end result so I don't have to deal with dynamic array, so ended up
# calculating the needed positions for indexes like this, not the prettiest solution because so many
# corner cases (pun intended)

def location_is_corner(location):
    spiral_level = spiral_level_for_memory_location(location)
    spiral_edge_size = 2 * spiral_level + 1
    spiral_level_max_location = spiral_edge_size ** 2
    spiral_level_min_location = spiral_level_max_location - (spiral_edge_size - 1) * 4 + 1
    distance_from_max_location = spiral_level_max_location - location
    return  location == spiral_level_min_location or \
            (location != spiral_level_max_location and \
            distance_from_max_location % (spiral_edge_size - 1) == 0)


def sum_indexes(location):
    if location == 1 or location == 2:
        return [0]

    spiral_level = spiral_level_for_memory_location(location)
    spiral_edge_size = 2 * spiral_level + 1
    spiral_level_max_location = spiral_edge_size ** 2
    spiral_level_min_location = spiral_level_max_location - (spiral_edge_size - 1) * 4 + 1
    spiral_level_max_edges = 1 + spiral_level * 4
    distance_from_max_location = spiral_level_max_location - location

    edges_from_max_location = floor(distance_from_max_location / (spiral_edge_size - 1))
    current_edge = spiral_level_max_edges - edges_from_max_location
    # Force minimum location to previous edge to get correct offset calculation
    current_edge -= 1 if location == spiral_level_min_location else 0
    offset_to_previous_level = 2 * current_edge - 3
    previous_level_location = int(location - offset_to_previous_level)

    if location_is_corner(location):
        return [location - 1, previous_level_location - 1]

    location_is_after_corner = location_is_corner(location - 1)
    location_is_before_corner = location_is_corner(location + 1)
    
    if location_is_after_corner and location_is_before_corner:
        return [location - 2, location - 1, previous_level_location]
    elif location_is_before_corner:
        return [
            location - 1, 
            previous_level_location - 1, 
            previous_level_location
        ]
    elif location_is_after_corner:
        return [
            location - 2, 
            location - 1, 
            previous_level_location, 
            previous_level_location + 1
        ]
    else:
        return [
            location - 1, 
            previous_level_location - 1, 
            previous_level_location, 
            previous_level_location + 1
        ]

def generate_next_spiral(spiral, target_value):
    if spiral[-1] > target_value:
        return spiral

    next_spiral_location = len(spiral) + 1
    indexes = sum_indexes(next_spiral_location)
    memory_values = ([spiral[x-1] for x in indexes])
    spiral.append(sum(memory_values))
    return generate_next_spiral(spiral, target_value)

target_memory_value = 289326
spiral = [1]
final_spiral = generate_next_spiral(spiral, target_memory_value)

print("First value greater than target value is: {}".format(final_spiral[-1]))
