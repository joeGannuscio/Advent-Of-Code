def main():
    orbits = readInput('Inputs/day6.txt')
    orbitDict = {o[1]:o[0] for o in orbits}
    part1(orbitDict) 
    part2(orbitDict)  

def part1(orbits):
    sum = 0

    for key in orbits:
        node = orbits.get(key, None)
        while node:
            sum += 1
            node = orbits.get(node, None)
    print(sum)

def part2(orbits):
    you = getPath(orbits, 'YOU')
    santa = getPath(orbits, 'SAN')
    print(len(you ^ santa))

def getPath(orbits, destination):
    path = []
    while destination != 'COM':
        path.append(orbits[destination])
        destination = orbits[destination]
    return set(path)

def readInput(path):
    input = []
    with open(path) as file:
        for line in file:
            input.append(line.strip('\n').split(')'))
    return input

if __name__ == '__main__':
    main()