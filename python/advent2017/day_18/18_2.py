from collections import namedtuple, defaultdict

Instruction = namedtuple('Instruction', 'type register parameter')
Program = namedtuple(
    'Program', 
    'registers instructions execution_position in_queue out_queue, waiting_for_value sends'
)

def parse_instruction(instruction_string):
    split = instruction_string.split(' ')
    instruction_type = split[0]
    register = split[1]

    if instruction_type == 'snd':
        return Instruction('send', register, None)
    elif instruction_type == 'set':
        return Instruction('set', register, split[2])
    elif instruction_type == 'add':
        return Instruction('add', register, split[2])
    elif instruction_type == 'mul':
        return Instruction('multiply', register, split[2])
    elif instruction_type == 'mod':
        return Instruction('modulo', register, split[2])
    elif instruction_type == 'rcv':
        return Instruction('receive', register, None)
    elif instruction_type == 'jgz':
        return Instruction('conditional_jump', register, split[2])

def execute_instruction(program):
    instruction = program.instructions[program.execution_position]
    try:
        register_value = int(instruction.register)
    except:
        register_value = program.registers[instruction.register]
    
    try:
        parameter = int(instruction.parameter)
    except:
        parameter = program.registers[instruction.parameter]

    wait_for_value = False
    sends_increment = 0
    execution_position_increment = 0
    if instruction.type == 'send':
        sends_increment = 1
        execution_position_increment = 1
        program.out_queue.append(register_value)
    elif instruction.type == 'set':
        execution_position_increment = 1
        program.registers[instruction.register] = parameter
    elif instruction.type == 'add':
        execution_position_increment = 1
        program.registers[instruction.register] += parameter
    elif instruction.type == 'multiply':
        execution_position_increment = 1
        program.registers[instruction.register] *= parameter
    elif instruction.type == 'modulo':
        execution_position_increment = 1
        program.registers[instruction.register] %= parameter
    elif instruction.type == 'receive':
        if len(program.in_queue) > 0:
            execution_position_increment = 1
            program.registers[instruction.register] = program.in_queue.pop(0)
        else:
            wait_for_value = True
    elif instruction.type == 'conditional_jump':
        execution_position_increment = parameter if register_value > 0 else 1

    return Program(
        program.registers,
        program.instructions,
        program.execution_position + execution_position_increment,
        program.in_queue,
        program.out_queue,
        wait_for_value,
        program.sends + sends_increment
    )

def can_execute(program):
    execution_position_valid = 0 <= program.execution_position < len(program.instructions)
    must_wait = program.waiting_for_value and len(program.in_queue) == 0
    return execution_position_valid and not must_wait

instructions = [parse_instruction(x.rstrip()) for x in open('input', 'r').readlines()]
registers_0 = defaultdict(int)
registers_1 = defaultdict(int)
registers_1['p'] = 1
in_queue_0 = []
in_queue_1 = []
programs = [
    Program(registers_0, instructions, 0, in_queue_0, in_queue_1, False, 0),
    Program(registers_1, instructions, 0, in_queue_1, in_queue_0, False, 0)
]

while any(map(can_execute, programs)):
    programs = [execute_instruction(x) if can_execute(x) else x for x in programs]

for i in range(0, len(programs)):
    print("Program {} sent a value {} times".format(i, programs[i].sends))
