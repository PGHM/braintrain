from collections import namedtuple
import sys

sys.setrecursionlimit(100000)

Component = namedtuple('Component', 'port1 port2')
Bridge = namedtuple('Bridge', 'strength length, last_port')

# Parsing

def parse_component(component_string):
    ports = component_string.strip().split('/')
    return Component(int(ports[0]), int(ports[1]))

# Helpers

def add_component_to_bridge(component, bridge):
    new_strength = bridge.strength + component.port1 + component.port2
    if component.port1 == bridge.last_port:
        return Bridge(new_strength, bridge.length + 1, component.port2)
    else:
        return Bridge(new_strength, bridge.length + 1, component.port1)

def component_fits_bridge(component, current_bridge):
    last_port = current_bridge.last_port
    return component.port1 == last_port or component.port2 == last_port

def components_removing_component(components, component):
    new_components = components.copy()
    new_components.remove(component)
    return new_components

# Part 1

def strongest_bridge_from_bridges(bridges, strongest_bridge):
    if len(bridges) == 0:
        return strongest_bridge

    new_bridges = bridges[1:]
    if bridges[0].strength > strongest_bridge.strength:
        strongest_bridge = bridges[0]

    return strongest_bridge_from_bridges(new_bridges, strongest_bridge)

def build_strongest_bridge(components, current_bridge):
    new_bridges = [
        build_strongest_bridge(
            components_removing_component(components, component),
            add_component_to_bridge(component, current_bridge)
        )
        for component in components
        if component_fits_bridge(component, current_bridge)
    ]
    
    if len(new_bridges) == 0:
        return current_bridge
    else:
        return strongest_bridge_from_bridges(new_bridges, new_bridges[0])

components = [parse_component(x) for x in open('input', 'r').readlines()]
bridge = Bridge(0, 0, 0)
final_answer = build_strongest_bridge(components, bridge).strength
print("Strongest bridge has the strength of {}".format(final_answer))

# Part 2

def longest_bridge_from_bridges(bridges, longest_bridge):
    if len(bridges) == 0:
        return longest_bridge

    new_bridges = bridges[1:]
    if (bridges[0].length > longest_bridge.length or 
       (bridges[0].length == longest_bridge.length and 
           bridges[0].strength > longest_bridge.strength)):
        longest_bridge = bridges[0]

    return longest_bridge_from_bridges(new_bridges, longest_bridge)

def build_longest_bridge(components, current_bridge):
    new_bridges = [
        build_longest_bridge(
            components_removing_component(components, component),
            add_component_to_bridge(component, current_bridge)
        )
        for component in components
        if component_fits_bridge(component, current_bridge)
    ]
    
    if len(new_bridges) == 0:
        return current_bridge
    else:
        return longest_bridge_from_bridges(new_bridges, new_bridges[0])

final_answer = build_longest_bridge(components, bridge).strength
print("Longest bridge has the strength of {}".format(final_answer))
