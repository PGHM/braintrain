from collections import namedtuple, defaultdict
import operator
import sys

sys.setrecursionlimit(100000)

Instruction = namedtuple('Instruction', 'register operator value condition')
Condition = namedtuple('Condition', 'register operator value')

def parse_operator(operator_string):
    if operator_string == 'inc':
        return operator.add
    elif operator_string == 'dec':
        return operator.sub
    elif operator_string == '>':
        return operator.gt
    elif operator_string == '>=':
        return operator.ge
    elif operator_string == '<':
        return operator.lt
    elif operator_string == '<=':
        return operator.le
    elif operator_string == '==':
        return operator.eq
    elif operator_string == '!=':
        return operator.ne
    else:
        raise Exception('Unknown operator')

def parse_condition(register, operator_string, value_string):
    return Condition(register, parse_operator(operator_string), int(value_string))

def parse_instruction(configration_string):
    parts = configration_string.split(' ')
    register = parts[0]
    operator = parse_operator(parts[1])
    value = int(parts[2])
    condition = parse_condition(parts[4], parts[5], parts[6])
    return Instruction(register, operator, value, condition)

def apply_instructions(registers, instructions, max_register_value):
    if len(instructions) == 0:
        return registers, max_register_value

    instruction = instructions.pop(0)
    condition_register_value = registers[instruction.condition.register]
    if instruction.condition.operator(condition_register_value, instruction.condition.value):
        target_register_value = registers[instruction.register]
        target_register_value = instruction.operator(target_register_value, instruction.value)
        registers[instruction.register] = target_register_value
        max_register_value = max(max_register_value, target_register_value)

    return apply_instructions(registers, instructions, max_register_value)

instructions = [parse_instruction(x.rstrip()) for x in open('input', 'r').readlines()]
registers = defaultdict(lambda: 0)
registers, max_register_value = apply_instructions(registers, instructions, -sys.maxsize)
max_final_register_value = max(registers.values())

print("Maximum final value in any register is {}".format(max_final_register_value))
print("Maximum value at any point in register was {}".format(max_register_value))

