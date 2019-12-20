def shift_array_by(array, amount):
    return array[amount:] + array[:amount]

def solve_captcha(array, shifted_array):
    pairs = zip(array, shifted_array)
    verified_values = [x if x == y else 0 for x, y in pairs]
    return sum(verified_values)

numbers = [int(x) for x in open('input', 'r').read().rstrip()]
first_captcha = solve_captcha(numbers, shift_array_by(numbers, 1))
second_captcha = solve_captcha(numbers, shift_array_by(numbers, len(numbers) / 2))

print("First part captcha: {}".format(first_captcha))
print("Second part captcha: {}".format(second_captcha))
