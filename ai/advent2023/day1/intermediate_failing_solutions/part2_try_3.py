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
        line = line.strip()
        words = line.split()
        first_word = words[0]
        last_word = words[-1]
        if first_word in digit_words:
            first_digit = digit_words[first_word]
        else:
            first_digit = next((char for char in first_word if char.isdigit()), None)
        if last_word in digit_words:
            last_digit = digit_words[last_word]
        else:
            last_digit = next((char for char in reversed(last_word) if char.isdigit()), None)
        if first_digit and last_digit:
            calibration_value = int(first_digit + last_digit)
            print(f'Calibration value for line "{line}": {calibration_value}')
            total += calibration_value
    print(f'Total sum of calibration values: {total}')

# Example data
lines = [
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen'
]

calculate_calibration_values(lines)
