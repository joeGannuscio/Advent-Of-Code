import math

def main():
    inputs = readInput('Inputs/day1.txt')
    part1(inputs)
    part2(inputs)
    
def part1(inputs):
    sum = 0
    for value in inputs:
        sum += calculateFuel(float(value))
    print(sum)

def part2(inputs):
    sum = 0
    for value in inputs:
        sum += calculateTotalModuleFuel(float(value))
    print(sum)


def calculateTotalModuleFuel(mass):
    totalFuel = calculateFuel(mass)
    fuelRequired = totalFuel

    while(calculateFuel(fuelRequired) > 0):
        fuelRequired = calculateFuel(fuelRequired)
        totalFuel += fuelRequired

    return totalFuel

def readInput(path):
    with open(path) as file:
        lines = file.readlines()
        return [line.strip() for line in lines]

def calculateFuel(mass):
    return math.floor(mass/3)-2

if (__name__ == '__main__'):
    main()