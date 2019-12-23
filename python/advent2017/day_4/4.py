passphrases = [x.rstrip() for x in open('input', 'r').readlines()]
passphrases = [x.split(' ') for x in passphrases]
valid_passphrases = [x for x in passphrases if len(set(x)) == len(x)]

print("{} passphrases are valid for part 1".format(len(valid_passphrases)))

passphrases = [[frozenset(x) for x in passphrase] for passphrase in passphrases]
valid_passphrases = [x for x in passphrases if len(set(x)) == len(x)]

print("{} passphrases are valid for part 2".format(len(valid_passphrases)))
