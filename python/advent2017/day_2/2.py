def checksum_value_from_row(row):
    return sum([x / y for x in row for y in row if x % y == 0 and x != y])

lines = open('input', 'r').readlines()
spreadsheet = [x.rstrip().split('\t') for x in lines]
spreadsheet = [[int(x) for x in row] for row in spreadsheet]
checksum_values = [abs(max(x) - min(x)) for x in spreadsheet]
print("Checksum for part 1 is: {}".format(sum(checksum_values)))

checksum_values = [checksum_value_from_row(x) for x in spreadsheet]
print("Checksum for part 2 is: {}".format(sum(checksum_values)))
