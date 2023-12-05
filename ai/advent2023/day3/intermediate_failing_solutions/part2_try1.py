def solve_puzzle(filename):
    with open(filename, 'r') as f:
        lines = [list(line.strip()) for line in f.readlines()]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    total = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '*':
                # Check all directions for part numbers
                part_numbers = []
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < len(lines) and 0 <= ny < len(lines[i]) and lines[nx][ny].isdigit():
                        # Check if the digit is part of a multi-digit number
                        num = ''
                        k = ny
                        while k < len(lines[i]) and lines[nx][k].isdigit():
                            num += lines[nx][k]
                            k += 1
                        num = int(num)
                        part_numbers.append(num)
                if len(part_numbers) == 2:
                    total += part_numbers[0] * part_numbers[1]
                    print(f"Adding {part_numbers[0]} * {part_numbers[1]} to total")
    return total

print(solve_puzzle("puzzle_input.txt"))
