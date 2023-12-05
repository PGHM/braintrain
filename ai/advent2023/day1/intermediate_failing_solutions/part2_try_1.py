def calculate_calibration_values(lines):
    digit_words = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    total = 0
    for line in lines:
        for word, digit in digit_words.items():
            line = line.replace(word, digit)
        first_digit = next((char for char in line if char.isdigit()), None)
        last_digit = next((char for char in reversed(line) if char.isdigit()), None)
        if first_digit and last_digit:
            calibration_value = int(first_digit + last_digit)
            print(f'Calibration value for line "{line.strip()}": {calibration_value}')
            total += calibration_value
    print(f'Total sum of calibration values: {total}')

# Example data
lines = [
    'two1nine\n',
    'eightwothree\n',
    'abcone2threexyz\n',
    'xtwone3four\n',
    '4nineeightseven2\n',
    'zoneight234\n',
    '7pqrstsixteen\n'
]

calculate_calibration_values(lines)
