from collections import namedtuple, defaultdict

Instruction = namedtuple('Instruction', 'type register parameter')
Result = namedtuple('Result', 'instruction_type value')

def parse_instruction(instruction_string):
    split = instruction_string.split(' ')
    instruction_type = split[0]
    register = split[1]

    if instruction_type == 'snd':
        return Instruction('play', register, None)
    elif instruction_type == 'set':
        return Instruction('set', register, split[2])
    elif instruction_type == 'add':
        return Instruction('add', register, split[2])
    elif instruction_type == 'mul':
        return Instruction('multiply', register, split[2])
    elif instruction_type == 'mod':
        return Instruction('modulo', register, split[2])
    elif instruction_type == 'rcv':
        return Instruction('conditional_recover', register, None)
    elif instruction_type == 'jgz':
        return Instruction('conditional_jump', register, split[2])

def apply_instruction(registers, program, execution_position):
    instruction = program[execution_position]
    register_value = registers[instruction.register]
    try:
        parameter = int(instruction.parameter)
    except:
        parameter = registers[instruction.parameter]

    result = None
    if instruction.type == 'play':
        execution_position += 1
        result = Result(instruction.type, register_value)
    elif instruction.type == 'set':
        execution_position += 1
        registers[instruction.register] = parameter
    elif instruction.type == 'add':
        execution_position += 1
        registers[instruction.register] += parameter
    elif instruction.type == 'multiply':
        execution_position += 1
        registers[instruction.register] *= parameter
    elif instruction.type == 'modulo':
        execution_position += 1
        registers[instruction.register] %= parameter
    elif instruction.type == 'conditional_recover':
        execution_position += 1
        result = Result(instruction.type, None) if register_value != 0 else None
    elif instruction.type == 'conditional_jump':
        execution_position_offset = parameter if register_value > 0 else 1
        execution_position += execution_position_offset

    return (registers, execution_position, result)

program = [parse_instruction(x.rstrip()) for x in open('input', 'r').readlines()]
execution_position = 0
last_frequency = None
registers = defaultdict(int)

while 0 <= execution_position < len(program):
    registers, execution_position, result = apply_instruction(
        registers, 
        program, 
        execution_position
    )

    if result:
        if result.instruction_type == 'play':
            last_frequency = result.value
        elif result.instruction_type == 'conditional_recover':
            break

print("The last frequency was {}".format(last_frequency))
