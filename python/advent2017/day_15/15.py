from itertools import accumulate

a = 679
b = 771
divider = 2147483647
iterations = 40000000

generate_a = lambda a: a * 16807 % divider
generate_b = lambda b: b * 48271 % divider
lowest_16_bits = lambda x: x & 0xFFFF

iteration = 0
matches = 0
while iteration < iterations:
    a = generate_a(a)
    b = generate_b(b)
    if lowest_16_bits(a) == lowest_16_bits(b):
        matches += 1
    
    iteration += 1

print("There was {} matches".format(matches))

def generate_a_part2():
    a = 679
    while True:
       a = generate_a(a)
       if a % 4 == 0:
           yield a

def generate_b_part2():
    b = 771
    while True:
       b = generate_b(b)
       if b % 8 == 0:
           yield b

iterations = 5000000
generator_a = generate_a_part2()
generator_b = generate_b_part2()

iteration = 0
matches = 0
while iteration < iterations:
    a = next(generator_a)
    b = next(generator_b)
    if lowest_16_bits(a) == lowest_16_bits(b):
        matches += 1
    
    iteration += 1

print("There was {} matches".format(matches))
