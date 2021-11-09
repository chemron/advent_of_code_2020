# https://adventofcode.com/2020/day/11
import numpy as np
import os
import time

with open("input.txt", "r") as f:
    finput = f.read()


class seating():
    def __init__(self, finput) -> None:
        self.as_string = finput.strip("\n")
        self.as_arr = self._get_arr()
        self.shape = self.as_arr.shape

    def iterate(self):

        n = 0
        new_layout = self.step()
        while not np.array_equal(new_layout, self.as_arr):
            # clear console before printing
            os.system('clear')
            print(self)
            print(n)

            # update
            self.as_arr = new_layout
            self.as_string = str(self)
            new_layout = self.step()
            n += 1
            time.sleep(0.1)

        # no. of occupied seats
        n_occupied = self.as_string.count("#")
        print(f"There are {n_occupied} occupied seats.")

    def step(self):
        new_layout = np.full(self.shape, ".")
        n, m = self.shape
        for i in range(n):
            for j in range(m):
                new_layout[i, j] = self._get_new_status((i, j))

        return new_layout

    def _get_arr(self):
        # list of rows
        rows = self.as_string.split()
        # matrix of layout
        seats = list([list(row) for row in rows])
        # convert to numpy array
        seats = np.array(seats)

        return seats

    def _get_new_status(self, coord):
        i, j = coord
        # adjacent steps (Compass coords)
        N = (-1, 0)
        NE = (-1, 1)
        E = (0, 1)
        SE = (1, 1)
        S = (1, 0)
        SW = (1, -1)
        W = (0,  - 1)
        NW = (-1, -1)

        adjacent_steps = [N, NE, E, SE, S, SW, W, NW]
        status = self.as_arr[i, j]
        adjacent_status = [
            self._get_diagonal_status(
                (coord[0] + step[0], coord[1] + step[1]), step
            ) for step in adjacent_steps]

        # Floor (.) never changes
        if status == ".":
            return "."
        # If a seat is empty (L) and there are no occupied
        # seats adjacent to it, the seat becomes occupied
        elif (status == "L") & ("#" not in adjacent_status):
            return "#"
        # If a seat is occupied (#) and four or more seats
        # adjacent to it are also occupied, the seat becomes empty.
        elif (status == "#") & (adjacent_status.count("#") >= 5):

            return "L"
        # Otherwise, the seat's state does not change.
        return status

    def _get_diagonal_status(self, coord, step):
        n, m = self.shape
        i, j = coord
        di, dj = step

        if self._is_over_edge(coord):
            return "."

        status = self._get_status(coord)
        next_coord = (i + di, j + dj)

        if status == ".":
            return self._get_diagonal_status(next_coord, step)

        else:
            return status

    def _is_over_edge(self, coord):
        n, m = self.shape
        i, j = coord
        return (i < 0) | (i >= n) | (j < 0) | (j >= m)

    def _get_status(self, coord):
        # get status of seat at index i,j
        if self._is_over_edge(coord):
            return "."
        else:
            return self.as_arr[coord]

    def __str__(self) -> str:
        # list of rows
        rows = ["".join(row) for row in self.as_arr]
        # combine rows:
        return "\n".join(rows)


seat_layout = seating(finput)
# print(seat_layout._get_diagonal_status((0, 0), (-1, 0)))
seat_layout.iterate()
