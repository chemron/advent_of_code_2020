# https://adventofcode.com/2020/day/12
import os

# Part 1


class movement:
    def __init__(self) -> None:
        # use complex numbers to represent position and location
        # positive Re = East
        # positive Im = North
        self.position = 0
        # start facing east (x, y)
        self.facing = 1

        # which actions correspond to strings
        self.move_dict = {
            "N": self.N,
            "S": self.S,
            "E": self.E,
            "W": self.W,
            "L": self.L,
            "R": self.R,
            "F": self.F
        }

    # action functions
    def N(self, value):
        self.position += value * 1j

    def S(self, value):
        self.position += value * (-1j)

    def E(self, value):
        self.position += value * 1

    def W(self, value):
        self.position += value * -1

    def L(self, value):
        rotations = value//90
        self.facing *= 1j ** rotations

    def R(self, value):
        rotations = -value//90

        self.facing *= 1j ** rotations

    def F(self, value):
        self.position += value * self.facing

    def move(self, input):
        os.system('clear')
        print(self)
        print(input[:-1])
        action = input[0]
        value = int(input[1:])

        # get function for action
        action_function = self.move_dict[action]
        # move
        action_function(value)
        print(self)

    def get_distance(self):
        dist = abs(self.position.real) + abs(self.position.imag)
        return int(dist)

    def __str__(self) -> str:
        string = f"Position: {self.position}\nFacing: {self.facing}"
        return string


ferry = movement()
# get input and move
with open("input.txt") as f:
    for line in f:
        ferry.move(line)
        # input()

print(f"Distance: {ferry.get_distance()}")
