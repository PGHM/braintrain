def solve_puzzle(filename):
    with open(filename, 'r') as f:
        lines = [list(line.strip()) for line in f.readlines()]

    symbols = ['*', '#', '+', '$']
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    total = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j].isdigit():
                # Check if the digit is part of a multi-digit number
                if (j > 0 and lines[i][j-1].isdigit()) or (j < len(lines[i])-1 and lines[i][j+1].isdigit()):
                    continue
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < len(lines) and 0 <= ny < len(lines[i]) and lines[nx][ny] in symbols:
                        # Sum all the digits of the multi-digit number
                        k = j
                        while k < len(lines[i]) and lines[i][k].isdigit():
                            total += int(lines[i][k])
                            k += 1
                        break
    return total

print(solve_puzzle("puzzle_input.txt"))
