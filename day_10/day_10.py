# https://adventofcode.com/2020/day/10
import numpy as np


f = open('input.txt', 'r')
adapters = f.read().split()
adapters = list(map(int, adapters))
adapters.sort()
# start at zero, end at end + 3
start = 0
end = adapters[-1] + 3

differences = np.array(adapters + [end]) - \
              np.array([start] + adapters)

# no. one jolt differences
n_one_j = len(np.where(differences==1)[0])

# no. three jolt differences
n_three_j = len(np.where(differences==3)[0])

print(f'# 1-jolt diff x # 3-jolt diff = {n_one_j*n_three_j} ')

# part 2

# num_ways[i] = number of ways to connect to adapter with voltage i
num_ways = np.zeros(adapters[-1] + 1, dtype=np.int64)

# one way to connect to the zeroth adapter (the outlet)
num_ways[0] = 1

for i in range(1, adapters[-1] + 1):
    if i in adapters:
        left = max(0, i-3)
        n = np.sum(num_ways[left:i])
        num_ways[i] = n
    else:
        num_ways[i] = 0

print(f"Number of arrangements: {num_ways[-1]}")
