def main():
    input = readInput('Inputs/day3.txt')
    part1(input)
    part2(input)

def part1(input):
    wire1 = processWireCoords(input[0])
    wire2 = processWireCoords(input[1])
    wire1Coords = []
    wire2Coords = []
    
    for point in wire1:
        wire1Coords.append((point[0], point[1]))
        
    for point in wire2:
        wire2Coords.append((point[0], point[1])) 
    
    intersect = (set(wire1Coords) & set(wire2Coords))
    dists = []
    for coord in intersect:
        if (calculateManhattanDistance((0,0), coord) != 0):
            dists.append(calculateManhattanDistance((0,0), coord))
    print(min(dists))
    
def part2(input):
    wire1 = processWireCoords(input[0])
    wire2 = processWireCoords(input[1])
    wire1Coords = []
    wire2Coords = []
    shared = {}
    
    for point in wire1:
        wire1Coords.append((point[0], point[1]))
        
    for point in wire2:
        wire2Coords.append((point[0], point[1])) 
    
    intersect = (set(wire1Coords) & set(wire2Coords))
    
    for point in wire1:
        if ((point[0], point[1]) in intersect and point[0] != 0 and point[1] != 0):
            shared[(point[0], point[1])] = point[2]
                
    for point in wire2:
        if ((point[0], point[1]) in intersect):
            if ((point[0], point[1]) in intersect and (point[0], point[1]) in shared and point[0] != 0 and point[1] != 0):
                shared[(point[0], point[1])] = shared[(point[0], point[1])] + point[2]
                
    print(min(shared.values()))
    
def calculateManhattanDistance(coord1, coord2):
    return(abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1]))

def processWireCoords(wire):
    currentCoord = (0,0,0) #x, y, stepcount
    currentCoords = []
    for direction in wire.split(','):
        dir = direction[:1]
        dist = int(direction[1:])
        currentCoords.extend(getCoordinates(dir, dist, currentCoord))
        currentCoord = currentCoords[-1]
    return currentCoords
           
def getCoordinates(direction, distance, currentCoord):
    if (direction == 'U'):
        return [(currentCoord[0], currentCoord[1] + i, currentCoord[2] + i) for i in range(distance+1)]
    elif (direction == 'D'):
        return [(currentCoord[0], currentCoord[1] - i, currentCoord[2] + i) for i in range(distance+1)]
    elif (direction == 'R'):
        return [(currentCoord[0] + i, currentCoord[1], currentCoord[2] + i) for i in range(distance+1)]
    elif (direction == 'L'):
        return [(currentCoord[0] - i, currentCoord[1], currentCoord[2] + i) for i in range(distance+1)]
    else:
        print('error')
        return

def readInput(path):
    with open(path) as file:
        input = []
        for line in file:
            input.append(line.strip('\n'))
        return input

if __name__ == '__main__':
    main()
