# https://adventofcode.com/2020/day/3
import numpy as np


def terrain_to_binary(char: str):
    if char == ".":
        return 0
    elif char == "#":
        return 1
    else:
        raise SyntaxError(f"Input must be \'.\' or \'#\', not {char}")


f = open('input.txt', 'r')
terrain = []
# read into rows
for row in f:
    bi_row = [terrain_to_binary(char) for char in row.strip()]
    terrain.append(bi_row)


terrain = np.array(terrain)


nrows, ncols = terrain.shape

# slope
slopes = np.array([[1, 1],
                   [3, 1],
                   [5, 1],
                   [7, 1],
                   [1, 2]
                   ], dtype=int)


tree_counts = np.zeros(len(slopes), dtype=int)

for i, slope in enumerate(slopes):
    dx, dy = slope
    path = np.zeros((nrows, ncols))

    dt = np.arange(np.ceil(nrows/dy), dtype=int)
    x_coords = (dx * dt) % ncols
    y_coords = dy * dt
    coords = np.stack((x_coords, y_coords), axis=-1)
    for x, y in coords:
        path[y, x] = 1

    tree_count = np.sum(path * terrain)
    print(f"Slope: {slope}, Tree-count: {tree_count:.0f}")
    tree_counts[i] = tree_count

tree_product = np.prod(tree_counts)
print(f"Product: {tree_product}")

# # traverse mountain:
# while y < len(data):
#     # Tree or open
#     terrain = data[y][x]
#     # if tree
#     if terrain == "#":
#         tree_count += 1
#         data[y][x] = 'X'
#     else:
#         data[y][x] = 'O'

#     x += dx
#     x = x % width
#     y += dy

# f.close()


# print(f"Tree count: {tree_count}")

# f = open('output.txt', 'w+')
# for row in data:
#     f.write(f"{''.join(row)}\n")
# f.close()
