import sys
sys.setrecursionlimit(100000)

def make_configuration_from(memory_banks):
    return ''.join([str(x) for x in memory_banks])

def rebalance_memory_banks(memory_banks, configurations_encountered, redistributions_needed):
    max_blocks = max(memory_banks)
    max_bank_index = memory_banks.index(max_blocks)
    memory_banks[max_bank_index] = 0

    memory_banks = redistribute_blocks(memory_banks, max_bank_index + 1, max_blocks)
    redistributions_needed += 1

    new_configuration = make_configuration_from(memory_banks)
    if new_configuration in configurations_encountered:
        cycle_size = redistributions_needed - configurations_encountered[new_configuration]
        return (redistributions_needed, cycle_size)
   
    configurations_encountered[new_configuration] = redistributions_needed
    return rebalance_memory_banks(memory_banks, configurations_encountered, redistributions_needed)

def redistribute_blocks(memory_banks, position, blocks_left):
    if position >= len(memory_banks):
        position = 0

    memory_banks[position] += 1
    blocks_left -= 1

    if blocks_left == 0:
        return memory_banks

    return redistribute_blocks(memory_banks, position + 1, blocks_left)

memory_banks = [int(x.rstrip()) for x in open('input', 'r').read().split('\t')]
redistributions_needed, cycle_size = rebalance_memory_banks(memory_banks, dict(), 0)

print("{} redistributions were needed to get infinite loop".format(redistributions_needed))
print("Cycle size of the infinite loop is {}".format(cycle_size))
