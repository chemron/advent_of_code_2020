# https://adventofcode.com/2020/day/1
import numpy as np

input = np.loadtxt('input.txt', dtype=int)
target = 2020
input.sort()


def two_sum(input, target):
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


def three_sum(input, target):
    half = target//2
    n = len(input)
    for i in range(n):
        x = input[i]
        if x <= half:
            two_target = target - x
            two_list = np.delete(input, i)
            product, y, z = two_sum(two_list, two_target)
            if product:
                return x*product, x, y, z


print(two_sum(input, target)[0])
print(three_sum(input, target)[0])
