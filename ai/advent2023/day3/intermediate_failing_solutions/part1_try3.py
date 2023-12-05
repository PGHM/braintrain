def solve_puzzle(schematic):
    lines = [list(line) for line in schematic.split('\n') if line]

    symbols = ['*', '#', '+', '$']
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    total = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j].isdigit():
                # Check if the digit is part of a multi-digit number
                num = ''
                k = j
                while k < len(lines[i]) and lines[i][k].isdigit():
                    num += lines[i][k]
                    k += 1
                num = int(num)
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < len(lines) and 0 <= ny < len(lines[i]) and lines[nx][ny] in symbols:
                        total += num
                        break
    return total

schematic = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

print(solve_puzzle(schematic))
