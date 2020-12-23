from collections import namedtuple, defaultdict

Instruction = namedtuple('Instruction', 'type register parameter')
Result = namedtuple('Result', 'instruction_type value')

def parse_instruction(instruction_string):
    split = instruction_string.split(' ')
    instruction_type = split[0]
    register = split[1]

    if instruction_type == 'set':
        return Instruction('set', register, split[2])
    elif instruction_type == 'sub':
        return Instruction('sub', register, split[2])
    elif instruction_type == 'mul':
        return Instruction('multiply', register, split[2])
    elif instruction_type == 'jnz':
        return Instruction('conditional_jump', register, split[2])

def get_value(value_or_register, registers):
    try:
        return int(value_or_register)
    except:
        return registers[value_or_register]

def apply_instruction(registers, program, execution_position, multiplications):
    instruction = program[execution_position]
    parameter = get_value(instruction.parameter, registers)

    if instruction.type == 'set':
        execution_position += 1
        registers[instruction.register] = parameter
    elif instruction.type == 'sub':
        execution_position += 1
        registers[instruction.register] -= parameter
    elif instruction.type == 'multiply':
        execution_position += 1
        multiplications += 1
        registers[instruction.register] *= parameter
    elif instruction.type == 'conditional_jump':
        conditional_value = get_value(instruction.register, registers)
        execution_position_offset = parameter if conditional_value != 0 else 1
        execution_position += execution_position_offset

    return (registers, execution_position, multiplications)

program = [parse_instruction(x.rstrip()) for x in open('input', 'r').readlines()]
execution_position = 0
multiplications = 0
registers = defaultdict(int)

while 0 <= execution_position < len(program):
    registers, execution_position, multiplications = apply_instruction(
        registers, 
        program, 
        execution_position,
        multiplications
    )

print("We did {} multiplications".format(multiplications))

# Part 2

# See input_commented for information what the program actually does. Without
# introducing further instructions to the set it is terrible to try to
# optimize the assembly code itself. It is possible, but terrible, because the
# jump offsets are screwed every time you introduce new command and you'd have
# to. I tried a while with the optimized_input, but it was too painful

# Just a naive and quick implementation of prime check
def is_prime(n):
    if n < 2 or n % 2 == 0:
        return False 
    
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

not_primes = 0
for i in range(105700, 122701, 17):
    if not is_prime(i):
        not_primes += 1

print("There are {} not prime numbers in the set".format(not_primes))
