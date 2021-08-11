# https://adventofcode.com/2020/day/2
f = open('input.txt', 'r')


def is_valid_1(line):
    # range, character, password
    r, c, w = line.split(" ")
    low, high = [int(x) for x in r.split("-")]
    c = c[:-1]

    # letter count in password:
    count = w.count(c)
    return (low <= count) and (high >= count)


def is_valid_2(line):
    # positions, character, password
    p, c, w = line.split(" ")
    # indices for character postion
    p1, p2 = [int(x)-1 for x in p.split("-")]
    c = c[:-1]

    # letter count in password:
    return (w[p1] == c) ^ (w[p2] == c)


valid_count_1 = 0
valid_count_2 = 0
for line in f:
    if is_valid_1(line):
        valid_count_1 += 1
    if is_valid_2(line):
        valid_count_2 += 1

print(f'valid_count (first policy): {valid_count_1}')
print(f'valid_count (second policy): {valid_count_2}')

f.close()
