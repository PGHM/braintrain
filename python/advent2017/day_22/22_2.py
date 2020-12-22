from collections import namedtuple
from enum import Enum

Movement = namedtuple('Movement', 'diff_x diff_y')
Virus = namedtuple('Virus', 'node direction')
Node = namedtuple("Node", 'x y status')

class NodeStatus(Enum):
    CLEAN = '.'
    WEAKENED = 'W'
    INFECTED = '#'
    FLAGGED = 'F'

class TurnDirection(Enum):
    STRAIGHT = 0
    LEFT = -1
    RIGHT = 1
    REVERSE = 2

class CardinalDirection(Enum):
    NORTH = Movement(0, 1)
    EAST = Movement(1, 0)
    SOUTH = Movement(0, -1)
    WEST = Movement(-1, 0)

    def by_turning_to(self, turn_direction):
        all_directions = list(CardinalDirection)
        current_index = all_directions.index(self)
        index_after_turning = current_index + turn_direction.value
        return all_directions[index_after_turning % len(all_directions)]

def parse_infected_nodes(initial_grid, y, infected_nodes):
    if len(initial_grid) == 0:
        return infected_nodes

    row = enumerate(initial_grid[0])
    for node in row:
        if node[1]  == '#':
            infected_nodes[(node[0], y)] = Node(node[0], y, NodeStatus.INFECTED)
    
    return parse_infected_nodes(
        initial_grid[1:], 
        y - 1, 
        infected_nodes
    )

def burst(virus, unclean_nodes, infection_count):
    current_x = virus.node.x
    current_y = virus.node.y
    unclean_node = unclean_nodes.get((current_x, current_y), None)
    if unclean_node == None:
        turn_direction = TurnDirection.LEFT
        weakened_node = Node(current_x, current_y, NodeStatus.WEAKENED)
        unclean_nodes[(current_x, current_y)] = weakened_node
        node_infected = False
    else:
        if unclean_node.status == NodeStatus.WEAKENED:
            turn_direction = TurnDirection.STRAIGHT
            infected_node = Node(current_x, current_y, NodeStatus.INFECTED)
            unclean_nodes[(current_x, current_y)] = infected_node
            node_infected = True
        elif unclean_node.status == NodeStatus.INFECTED:
            turn_direction = TurnDirection.RIGHT
            flagged_node = Node(current_x, current_y, NodeStatus.FLAGGED)
            unclean_nodes[(current_x, current_y)] = flagged_node
            node_infected = False
        elif unclean_node.status == NodeStatus.FLAGGED: 
            turn_direction = TurnDirection.REVERSE
            unclean_nodes[(current_x, current_y)] = None
            node_infected = False

    new_cardinal_direction = virus.direction.by_turning_to(turn_direction)
    new_x = current_x + new_cardinal_direction.value.diff_x
    new_y = current_y + new_cardinal_direction.value.diff_y
    return (
        Virus(Node(new_x, new_y, None), new_cardinal_direction),
        unclean_nodes,
        infection_count + 1 if node_infected else infection_count
    )

initial_grid = [line.strip() for line in open('input', 'r').readlines()]
unclean_nodes = parse_infected_nodes(initial_grid, 0, {})
bursts = 10000000
start_x = len(initial_grid) // 2
start_y = -(len(initial_grid) // 2)
start_node = Node(start_x, start_y, None)
virus = Virus(start_node, CardinalDirection.NORTH)
infection_count = 0

for i in range(0, bursts):
    if i % 10000 == 0:
        print(i)

    virus, unclean_nodes, infection_count = burst(
        virus, 
        unclean_nodes,
        infection_count
    )

print("{} nodes were infected because of new bursts".format(infection_count))
