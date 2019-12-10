import math

def main():
    input = readInput('Inputs/day10.txt')
    part1(input)
    
def part1(input):
    asteroids = GetAsteroidCoords(input)
    print(findBestAsteroidCount(asteroids))

def findBestAsteroidCount(asteroids):
    maxVisibleCount = 0
    for i in range(len(asteroids)):
        angles = []
        for j in range(len(asteroids)):
            if i == j:
                continue
            angle = math.atan2(asteroids[i][0] - asteroids[j][0], asteroids[i][1] - asteroids[j][1])

            if angle not in angles:
                angles.append(angle)
        
        if len(angles) > maxVisibleCount:
            maxVisibleCount = len(angles)
            asteroid = asteroids[i]
    
    print(f'bes asteroid: {asteroid}')
    return maxVisibleCount


def GetAsteroidCoords(input):
    asteroids = []
    x = 0
    y = 0
    for row in input:
        y = 0
        for char in row:
            if char == '#':
                asteroids.append((x,y))
            y += 1
        x += 1

    return asteroids

def readInput(path):
    with open(path) as file:
        input = []
        for line in file:
            input.append(line.strip('\n'))
        return input

if __name__ == '__main__':
    main()