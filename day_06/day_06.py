# https://adventofcode.com/2020/day/6
f = open('input.txt', 'r')
groups = f.read().split('\n\n')

total = 0

for group in groups:
    answers = [set(answer) for answer in group.split()]
    common = set(answers[0])

    for answer in answers[1:]:
        common = common & answer

    total += len(common)

print(f'Total: {total}')
