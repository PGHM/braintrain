from collections import namedtuple
from itertools import takewhile

Machine = namedtuple('Machine', 'tape cursor_position next_state states')
State = namedtuple('State', 'action_if_0 action_if_1')
Action = namedtuple('Action', 'write_value move_direction next_state')

# Parsing

def parse_states(input_lines, result):
    if len(input_lines) == 0:
        return result

    state_lines = list(takewhile(lambda x: x != '', input_lines))
    state_name = state_lines[0][-2]
    result[state_name] = parse_state(state_lines[1:])
    return parse_states(input_lines[len(state_lines) + 1:], result)

def parse_state(state_lines):
    action_if_0 = parse_action(state_lines[1:4])
    action_if_1 = parse_action(state_lines[5:8])
    return State(action_if_0, action_if_1)

def parse_action(action_lines):
    write_value = int(action_lines[0][-2])
    move_direction = action_lines[1][:-1].split(' ')[-1]
    next_state = action_lines[2][-2]
    return Action(write_value, move_direction, next_state)

# Part 1

def handle_action(action, machine):
    if action.move_direction == 'left':
        if machine.cursor_position == 0:
            new_tape = [0] + machine.tape
            new_tape[1] = action.write_value
            new_cursor_position = machine.cursor_position
        else:
            new_tape = machine.tape.copy()
            new_tape[machine.cursor_position] = action.write_value
            new_cursor_position = machine.cursor_position - 1

        return new_tape, new_cursor_position
    
    new_cursor_position = machine.cursor_position + 1
    if machine.cursor_position == len(machine.tape) - 1:
        new_tape = machine.tape + [0]
    else:
        new_tape = machine.tape.copy()

    new_tape[machine.cursor_position] = action.write_value
    return new_tape, new_cursor_position

def execute_one_step(machine):
    state = machine.states[machine.next_state]
    
    if machine.tape[machine.cursor_position] == 0:
        action = state.action_if_0
    else:
        action = state.action_if_1

    new_tape, new_cursor_position = handle_action(action, machine)
    return Machine(new_tape, new_cursor_position, action.next_state, states)

input_lines = [x.strip() for x in open('input', 'r').readlines()]
initial_state = input_lines[0][-2]
execution_steps = int(input_lines[1].split(' ')[-2])
states = parse_states(input_lines[3:], {})
machine = Machine([0], 0, initial_state, states)

for i in range(0, execution_steps):
    machine = execute_one_step(machine)

final_answer = len([x for x in machine.tape if x == 1])
print("Checksum is {}".format(final_answer))

# Part 2

print("50 stars achieved!")
