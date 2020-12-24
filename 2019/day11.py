from intcode import Intcode
from enum import Enum

def main():
    input = readInput('Inputs/day11.txt')
    part1(input)
    part2(input)

def part1(input):
    panels = runRobot(input, 0)
    print(len(panels))

def part2(input):
    panels = runRobot(input, 1)
    print(panels)
            

def runRobot(input, startColor):
    intcodeRunner = Intcode(input)
    robot = Robot()
    panels = {(0, 0): 0}

    while not intcodeRunner.done:
        if len(intcodeRunner.inputs) == 0:
            intcodeRunner.inputs.append(startColor)
        else:
            intcodeRunner.inputs.append(panels.get((robot.position[0], robot.position[1]), 0))
        intcodeRunner.run()

        color = intcodeRunner.outputs[-2]
        direction = intcodeRunner.outputs[-1]

        panels[(robot.position[0], robot.position[1])] = color
        robot.turn(direction)
        robot.move()
    return panels

class Directions(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

class Robot:
    def __init__(self):
        self.direction = Directions.UP
        self.position = [0,0]

    def turnLeft(self):
        if self.direction == Directions.UP:
            self.direction = Directions.LEFT
        elif self.direction == Directions.LEFT:
            self.direction = Directions.DOWN
        elif self.direction == Directions.DOWN:
            self.direction = Directions.RIGHT
        elif self.direction == Directions.RIGHT:
            self.direction = Directions.UP
    
    def turnRight(self):
        if self.direction == Directions.UP:
            self.direction = Directions.RIGHT
        elif self.direction == Directions.LEFT:
            self.direction = Directions.UP
        elif self.direction == Directions.DOWN:
            self.direction = Directions.LEFT
        elif self.direction == Directions.RIGHT:
            self.direction = Directions.DOWN

    def move(self):
        if self.direction == Directions.UP:
            self.position[1] += 1
        elif self.direction == Directions.DOWN:
            self.position[1] -= 1
        elif self.direction == Directions.RIGHT:
            self.position[0] += 1
        elif self.direction == Directions.LEFT:
            self.position[0] -= 1

    def turn(self, direction):
        if direction == 0:
            self.turnLeft()
        elif direction == 1:
            self.turnRight()


def readInput(path):
    with open(path) as file:
        line = file.readline()
        vals = line.split(',')
        return [int(i) for i in vals]

if __name__ == '__main__':
    main()