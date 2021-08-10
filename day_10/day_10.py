import numpy as np


f = open('test_input.txt', 'r')
adapters = f.read().split()
adapters = list(map(int, adapters))
adapters.sort()
# start at zero, end at end + 3
start = 0
end = adapters[-1] + 3

differences = np.array(adapters + [end]) - \
              np.array([start] + adapters)

print(differences)
# no. one jolt differences
n_one_j = 0

# no. three jolt differences
n_three_j = 0

for i, i_val in enumerate(adapters[:-1]):
    j = i + 1
    j_val = adapters[j]
    if j_val - i_val == 1:
        n_one_j += 1
    elif j_val - i_val == 3:
        n_three_j += 1

print(f'# 1-jolt diff x # 3-jolt diff = {n_one_j*n_three_j} ')
