def main():
    inputs = readInput('Inputs/day15.txt')
    print(inputs)

def readInput(path):
    with open(path) as file:
        line = file.readline()
        vals = line.split(',')
        return [int(i) for i in vals]

if __name__ == '__main__':
    main()