import operator
import sys
from functools import reduce

sys.setrecursionlimit(100000)

def main():
    transformations = [225, 171, 131, 2, 35, 5, 0, 13, 1, 246, 54, 97, 255, 98, 254, 110]
    numbers = list(range(0, 256))
    numbers = apply_transformations(transformations, numbers, 0, 0)

    print("The result of the check is {}".format(numbers[0] * numbers[1]))
    
    numbers_hash = knot_hash("225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110")

    print("The knot hash of the numbers is '{}'".format(numbers_hash))

def apply_transformations(transformations, numbers, position, extra_skip):
    if len(transformations) == 0:
        cut_position = len(numbers) - position
        return numbers[cut_position:] + numbers[:cut_position]

    transformation = transformations.pop(0)
    transformed = list(reversed(numbers[:transformation]))
    numbers = transformed + numbers[transformation:]

    move_amount = (transformation + extra_skip) % len(numbers)
    numbers = numbers[move_amount:] + numbers[:move_amount]
    return apply_transformations(
        transformations, 
        numbers, 
        (position + move_amount) % len(numbers), 
        extra_skip + 1
    )

def calculate_dense_hash(numbers, numbers_hash):
    if len(numbers) == 0:
        return numbers_hash

    numbers_to_be_densed = numbers[:16]
    densed = reduce(operator.xor, numbers_to_be_densed)
    numbers_hash += hex(densed)[2:].zfill(2)
    return calculate_dense_hash(numbers[16:], numbers_hash)

def knot_hash(input_string):
    rounds = 64
    numbers = list(range(0, 256))
    transformations = [ord(x) for x in input_string] + [17, 31, 73, 47, 23]
    transformations = transformations * rounds
    numbers = apply_transformations(transformations, numbers, 0, 0)
    return calculate_dense_hash(numbers, '')

if __name__== "__main__":
    main()
