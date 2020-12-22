from collections import namedtuple
from enum import Enum
import sys

sys.setrecursionlimit(100000)

Movement = namedtuple('Movement', 'diff_x diff_y')
Virus = namedtuple('Virus', 'node direction')
Node = namedtuple("Node", 'x y')

class TurnDirection(Enum):
    LEFT = -1
    RIGHT = 1

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
    new_infected_nodes = [Node(x[0], y) for x in row if x[1] == '#']
    return parse_infected_nodes(
        initial_grid[1:], 
        y - 1, 
        infected_nodes + new_infected_nodes
    )

def burst(virus, infected_nodes, bursts_left, infection_count):
    if bursts_left == 0:
        return infection_count

    virus_node_infected = virus.node in infected_nodes
    if virus_node_infected:
        turn_direction = TurnDirection.RIGHT
        current_node_index = infected_nodes.index(virus.node)
        head = infected_nodes[:current_node_index]
        tail = infected_nodes[current_node_index + 1:]
        new_infected_nodes = head + tail
    else:
        turn_direction = TurnDirection.LEFT
        new_infected_nodes = infected_nodes + [virus.node]

    new_cardinal_direction = virus.direction.by_turning_to(turn_direction)
    new_x = virus.node.x + new_cardinal_direction.value.diff_x
    new_y = virus.node.y + new_cardinal_direction.value.diff_y
    return burst(
        Virus(Node(new_x, new_y), new_cardinal_direction),
        new_infected_nodes,
        bursts_left - 1,
        infection_count + 1 if not virus_node_infected else infection_count
    )

initial_grid = [line.strip() for line in open('input', 'r').readlines()]
infected_nodes = parse_infected_nodes(initial_grid, 0, [])

bursts = 10000
start_node = Node(len(initial_grid) // 2, -(len(initial_grid) // 2))
virus = Virus(start_node, CardinalDirection.NORTH)
infection_count = burst(virus, infected_nodes, bursts, 0)

print("{} nodes were infected because of new bursts".format(infection_count))
