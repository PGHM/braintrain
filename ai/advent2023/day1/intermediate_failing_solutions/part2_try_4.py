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
        first_digit = None
        last_digit = None
        for word in words:
            if word in digit_words:
                if first_digit is None:
                    first_digit = digit_words[word]
                last_digit = digit_words[word]
            else:
                for char in word:
                    if char.isdigit():
                        if first_digit is None:
                            first_digit = char
                        last_digit = char
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
