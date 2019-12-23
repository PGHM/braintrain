# Tried to do with recursion but python does not like too much of it and
# crashes, so while loop then instead

code = [int(x.rstrip()) for x in open('input', 'r').readlines()]
code_length = len(code)
steps_taken = 0
position = 0

while 0 <= position < code_length:
    instruction = code[position]
    code[position] = instruction + 1
    position += instruction
    steps_taken += 1

print("Needed {} steps to get out of the code maze in part 1".format(steps_taken))

code = [int(x.rstrip()) for x in open('input', 'r').readlines()]
steps_taken = 0
position = 0

while 0 <= position < code_length:
    instruction = code[position]
    code[position] = instruction + 1 if instruction < 3 else instruction - 1
    position += instruction
    steps_taken += 1

print("Needed {} steps to get out of the code maze in part 2".format(steps_taken))
