def solve_puzzle(filename):
    with open(filename, 'r') as f:
        lines = [list(line.strip()) for line in f.readlines()]

    symbols = ['*', '#', '+', '$']
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    total = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j].isdigit():
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < len(lines) and 0 <= ny < len(lines[i]) and lines[nx][ny] in symbols:
                        total += int(lines[i][j])
                        break
    return total

print(solve_puzzle("puzzle_input.txt"))
