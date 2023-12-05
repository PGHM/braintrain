def calculate_calibration_values(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    total = 0
    for line in lines:
        first_digit = next((char for char in line if char.isdigit()), None)
        last_digit = next((char for char in reversed(line) if char.isdigit()), None)
        if first_digit and last_digit:
            total += int(first_digit + last_digit)
    return total

print(calculate_calibration_values('puzzle_input.txt'))
