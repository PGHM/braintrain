def solve_puzzle(filename):
    with open(filename, 'r') as f:
        lines = [list(line.strip()) for line in f.readlines()]

    symbols = ['*', '#', '+', '$']
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    total = 0

    for i in range(len(lines)):
        print(f"Processing row {i+1}")
        j = 0
        while j < len(lines[i]):
            if lines[i][j].isdigit():
                # Check if the digit is part of a multi-digit number
                num = ''
                k = j
                while k < len(lines[i]) and lines[i][k].isdigit():
                    num += lines[i][k]
                    k += 1
                num = int(num)
                # Check all digits of the number for adjacent symbols
                has_symbol = False
                for l in range(j, k):
                    for dx, dy in directions:
                        nx, ny = i + dx, l + dy
                        if 0 <= nx < len(lines) and 0 <= ny < len(lines[i]) and lines[nx][ny] in symbols:
                            has_symbol = True
                            break
                    if has_symbol:
                        break
                if has_symbol:
                    total += num
                    print(f"Adding {num} to total")
                j = k
            else:
                j += 1
    return total

print(solve_puzzle("puzzle_input.txt"))
