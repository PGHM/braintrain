import sys

sys.setrecursionlimit(100000)

def fill_buffer(circular_buffer, position, value, step_count):
    if value > 2017:
        return circular_buffer

    index = (position + step_count) % len(circular_buffer)
    circular_buffer.insert(index + 1, value)
    return fill_buffer(circular_buffer, index + 1, value + 1, step_count)

step_count = 386
circular_buffer = [0]
filled_buffer = fill_buffer(circular_buffer, 1, 1, step_count)
target_index = (filled_buffer.index(2017) + 1) % len(circular_buffer)
target_value = filled_buffer[target_index]

print("The value after last written value is {}".format(target_value))

def spinlock_value(step_limit):
    step = 0
    position = 0
    step_count = 386
    while step < step_limit:
        value = step + 1
        position = ((position + step_count) % value) + 1
        
        yield (value, position)
        
        step += 1

spinlock_value_generator = spinlock_value(50000000)
target_value = 0

for value, position in spinlock_value_generator:
    if position == 1:
        target_value = value

print("The value after position 0 is {}".format(target_value))
