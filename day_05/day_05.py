import numpy as np
from numpy.core.defchararray import array


def get_seat_id(seat):
    return int(seat_to_binary(seat), 2)


def seat_to_binary(string):
    b_string = ""
    for letter in string:
        if letter in ('F', 'L'):
            b_string += '0'
        else:
            b_string += '1'
    return b_string


f = open('input.txt', 'r')
seats = f.read().split()
f.close()

ids = list(map(get_seat_id, seats))
ids = np.sort(ids)
print(ids)

start = ids[0]
n = len(ids)
# find the index where the seat numbers skip one:
index = np.searchsorted(ids-start - np.arange(n), 0.5)
print(index + start)
