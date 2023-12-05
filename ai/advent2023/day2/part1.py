def solve_puzzle():
    with open('puzzle_input.txt', 'r') as file:
        games = file.readlines()

    possible_games = 0
    for game in games:
        game_id, rounds = game.split(': ')
        game_id = int(game_id.split(' ')[1])
        rounds = rounds.strip().split('; ')

        possible = True
        for round in rounds:
            cubes = round.split(', ')
            red = sum(int(cube.split(' ')[0]) for cube in cubes if 'red' in cube)
            green = sum(int(cube.split(' ')[0]) for cube in cubes if 'green' in cube)
            blue = sum(int(cube.split(' ')[0]) for cube in cubes if 'blue' in cube)

            if red > 12 or green > 13 or blue > 14:
                possible = False
                break

        if possible:
            possible_games += game_id

    return possible_games

print(solve_puzzle())
