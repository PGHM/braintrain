def calculate_calibration_values(filename):
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
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in lines:
        line = line.strip()
        first_digit = None
        last_digit = None
        for i in range(len(line)):
            for digit_word, digit_value in digit_words.items():
                if line[i:i+len(digit_word)] == digit_word:
                    if first_digit is None:
                        first_digit = digit_value
                    last_digit = digit_value
            if line[i].isdigit():
                if first_digit is None:
                    first_digit = line[i]
                last_digit = line[i]
        if first_digit and last_digit:
            calibration_value = int(first_digit + last_digit)
            print(f'Calibration value for line "{line}": {calibration_value}')
            total += calibration_value
    print(f'Total sum of calibration values: {total}')

# Call the function with your filename
calculate_calibration_values('puzzle_input.txt')
