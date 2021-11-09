# https://adventofcode.com/2020/day/12
import os

# Part 1


class movement:
    def __init__(self) -> None:
        # use complex numbers to represent position and location
        # positive Re = East
        # positive Im = North

        # ferry absolute position
        self.pos = 0
        # waypoint position relative to ferry
        # (starts 10 units east and 1 unit north relative to the ship)
        self.waypoint_pos = 10 + 1j

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
        self.waypoint_pos += value * 1j

    def S(self, value):
        self.waypoint_pos += value * (-1j)

    def E(self, value):
        self.waypoint_pos += value * 1

    def W(self, value):
        self.waypoint_pos += value * -1

    def L(self, value):
        rotations = value//90
        self.waypoint_pos *= 1j ** rotations

    def R(self, value):
        rotations = -value//90

        self.waypoint_pos *= 1j ** rotations

    def F(self, value):
        self.pos += value * self.waypoint_pos

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
        dist = abs(self.pos.real) + abs(self.pos.imag)
        return int(dist)

    def __str__(self) -> str:
        string = f"Ship: {self.pos}\nWaypoint: {self.waypoint_pos}"
        return string


ferry = movement()
# get input and move
with open("input.txt") as f:
    for line in f:
        ferry.move(line)

print(f"Distance: {ferry.get_distance()}")
