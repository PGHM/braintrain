from collections import namedtuple

Layer = namedtuple('Layer', 'depth range')

def parse_layer(layer_string):
    depth_string, range_string = layer_string.split(':')
    return Layer(int(depth_string), int(range_string))

def scanner_position_in_layer(layer, delay):
    round_time = (layer.range - 1) * 2
    half_round_time = layer.range - 1
    time_elapsed = layer.depth + delay
    normalized_time_elapsed = time_elapsed % round_time
    return half_round_time - abs(half_round_time - normalized_time_elapsed)

layers = [parse_layer(x.rstrip()) for x in open('input', 'r').readlines()]

severity_score = sum(
    [x.depth * x.range if scanner_position_in_layer(x, 0) == 0 else 0 for x in layers]
)

print("Severity score is {}".format(severity_score))

# Again too much recursion needed to do this recursively
delay = 0
while next(filter(lambda x: scanner_position_in_layer(x, delay) == 0, layers), None):
    delay += 1

print("Smallest delay that lets you go through uncaught is {}".format(delay))
