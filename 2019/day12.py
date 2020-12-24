from re import findall
import math
from functools import reduce

def main():
    inputs = readInput('Inputs/day12.txt')
    part1(inputs)
    part2(inputs)

def part1(inputs):
    moons = []
    for input in inputs:
        moons.append(Moon(input))

    for _ in range(1000):

        for i in range(3):
            for j in range(i + 1, 4):
                applyGravity(moons[i], moons[j])

        for moon in moons:
            applyVelocity(moon)

    systemEnergy = 0

    for moon in moons:
        pot = abs(moon.x) + abs(moon.y) + abs(moon.z)
        kin = abs(moon.vx) + abs(moon.vy) + abs(moon.vz)
        systemEnergy += (pot * kin)

    print(systemEnergy)

def part2(inputs):
    print('idk')
  
def applyGravity(moon1, moon2):
    if moon1.x > moon2.x:
        moon1.vx -= 1
        moon2.vx += 1
    elif moon1.x < moon2.x:
        moon1.vx += 1
        moon2.vx -= 1

    if moon1.y > moon2.y:
        moon1.vy -= 1
        moon2.vy += 1
    elif moon1.y < moon2.y:
        moon1.vy += 1
        moon2.vy -= 1

    if moon1.z > moon2.z:
        moon1.vz -= 1
        moon2.vz += 1
    elif moon1.z < moon2.z:
        moon1.vz += 1
        moon2.vz -= 1

def applyVelocity(moon):
    moon.x += moon.vx
    moon.y += moon.vy
    moon.z += moon.vz

def readInput(path):
    with open(path) as file:
        input = []
        for line in file:
            input.append([int(x) for x in findall(r'-?\d+', line)])
        return input

class Moon:
    def __init__(self, positions):
        self.x = positions[0]
        self.y = positions[1]
        self.z = positions[2]
        self.vx = 0
        self.vy = 0
        self.vz = 0

if __name__ == '__main__':
    main()