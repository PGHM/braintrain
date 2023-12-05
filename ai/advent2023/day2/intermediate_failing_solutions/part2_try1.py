def solve_puzzle():
    with open('puzzle_input.txt', 'r') as file:
        games = file.readlines()

    total_power = 0
    for game in games:
        game_id, rounds = game.split(': ')
        game_id = int(game_id.split(' ')[1])
        rounds = rounds.strip().split('; ')

        min_red, min_green, min_blue = 0, 0, 0
        for round in rounds:
            cubes = round.split(', ')
            red = max(int(cube.split(' ')[0]) for cube in cubes if 'red' in cube)
            green = max(int(cube.split(' ')[0]) for cube in cubes if 'green' in cube)
            blue = max(int(cube.split(' ')[0]) for cube in cubes if 'blue' in cube)

            min_red = max(min_red, red)
            min_green = max(min_green, green)
            min_blue = max(min_blue, blue)

        power = min_red * min_green * min_blue
        total_power += power

    return total_power

print(solve_puzzle())
