import sys
import re

sys.setrecursionlimit(100000)

def skip_garbage(stream, skipped_amount):
    if stream.startswith('>'):
        return stream[1:], skipped_amount

    if re.match(re.compile('^!.'), stream):
        return skip_garbage(stream[2:], skipped_amount)

    return skip_garbage(stream[1:], skipped_amount + 1)

def count_score(stream, group_level, score, skipped_garbage):
    if len(stream) == 0:
        return score, skipped_garbage
    
    if stream.startswith('{'):
        return count_score(stream[1:], group_level + 1, score, skipped_garbage)
    elif stream.startswith('}'):
        return count_score(stream[1:], group_level - 1, score + group_level, skipped_garbage)
    elif stream.startswith('<'):
        stream, skipped_amount = skip_garbage(stream[1:], 0)
        return count_score(stream, group_level, score, skipped_garbage + skipped_amount)

    return count_score(stream[1:], group_level, score, skipped_garbage)

stream = open('input', 'r').read().rstrip()

score, skipped_garbage = count_score(stream, 0, 0, 0)
print("Score of the stream is {}".format(score))
print("Skipped {} garbade charactes in the stream".format(skipped_garbage))
