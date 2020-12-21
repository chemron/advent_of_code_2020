import numpy as np


def is_valid(lst, target):
    # check if numbers in lst sum to target
    half = target//2
    n = len(input)
    for i in range(n):
        x = input[i]
        if x <= half:
            y = target - x
            j = np.searchsorted(input[i+1:], y)
            if input[j+i+1] == y:
                return x * y, x, y
    return 0, 0, 0


f = open('input.txt', 'r')

numbers = np.array(f.read().split())

# length of preamble
p_length = 5

# sort preamble
numbers[:p_length].sort()


# new list with insertion sort
for i in range(p_length, len(numbers)):
    sub_list = numbers[:i]
    target = numbers[i]
    if not is_valid(sub_list, target):
        print(target)
    # index to insert target to make numbers[:i+1] sorted
    insert_i = np.searchsorted(sub_list, target)
    numbers[:i+1] = np.hstack((numbers[:insert_i],
                               target,
                               numbers[insert_i:i]))
