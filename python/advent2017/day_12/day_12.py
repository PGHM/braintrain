import sys, random
from collections import namedtuple
from functools import reduce

sys.setrecursionlimit(100000)

Program = namedtuple('Program', 'name connections')

def main():
    programs = dict([parse_program(x.rstrip()) for x in open('input', 'r').readlines()])
    target_program = programs['0']
    group = get_group(target_program, programs, set())

    print("There is {} members in the group which '0' resides in".format(len(group)))
    
    program_names = set(programs.keys())
    groups = get_all_groups(program_names, programs, [])

    print("There are {} groups in total".format(len(groups)))

def parse_program(program_string):
    splitted = program_string.split('<->')
    name = splitted[0].strip()
    connections = [x.strip() for x in splitted[1].split(',')]
    return (name, Program(name, connections))

def get_group(program, all_programs, group_members):
    if program.name in group_members:
        return group_members

    group_members.add(program.name)
    connection_groups = [
        get_group(all_programs[x], all_programs, group_members) 
        for x 
        in program.connections
    ]
    reduce_function = lambda current_members, new_members: current_members.union(new_members)
    group_members = reduce(reduce_function, connection_groups, group_members)
    return group_members

def get_all_groups(program_names, all_programs, groups):
    if len(program_names) == 0:
        return groups

    random_program_name = random.sample(program_names, 1)[0] 
    group = get_group(all_programs[random_program_name], all_programs, set())
    program_names.difference_update(group)
    groups.append(group)
    return get_all_groups(program_names, all_programs, groups)

if __name__== "__main__":
    main()
