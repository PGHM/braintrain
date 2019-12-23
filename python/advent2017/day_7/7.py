import itertools

def parse_program(conf_string):
    name, rest = conf_string.split('(')
    name = name.strip()
    weight, rest = rest.split(')')
    rest = rest.replace(" -> ", "")
    weight = int(weight)

    children = rest.split(',') if len(rest) > 0 else []
    children = [x.strip() for x in children]
    return (name, {"name": name, "weight": weight, "children": children})

programs = dict([parse_program(x.rstrip()) for x in open('input', 'r').readlines()])
child_unflattened = [x["children"] for x in programs.values()]
children = list(itertools.chain.from_iterable(child_unflattened))
parent_program = next(filter(lambda x: x not in children, programs.keys()))

print("The parent of all the programs is '{}'".format(parent_program))

def populate_full_program_information(program_name, all_programs):
    program = all_programs[program_name]
    if len(program["children"]) == 0:
        program["full_weight"] = program["weight"]
        return program

    child_programs = [
        populate_full_program_information(child_name, all_programs)
        for child_name 
        in program["children"]
    ]
    program["children"] = child_programs
    program["full_weight"] = program["weight"] + sum([x["full_weight"] for x in program["children"]])
    return program

def find_unbalanced_weight(program, target_weight):
    children = program["children"]
    child_weights = [x["full_weight"] for x in children]
    unique_weights = set(child_weights)

    if len(unique_weights) <= 1:
        return target_weight - sum(child_weights)

    counts = [(x, child_weights.count(x)) for x in unique_weights]
    
    outlier_count = min([x[1] for x in counts])
    outlier_weight = next(filter(lambda x: x[1] == outlier_count, counts))[0] 
    outlier_child = children[child_weights.index(outlier_weight)]
    
    normal_count = max([x[1] for x in counts])
    normal_weight = next(filter(lambda x: x[1] == normal_count, counts))[0]
    
    return find_unbalanced_weight(outlier_child, normal_weight)

parent_program = populate_full_program_information(parent_program, programs)
unbalanced_weight = find_unbalanced_weight(parent_program, parent_program["full_weight"])

print("Unbalanced weight should weigh {}".format(unbalanced_weight))
