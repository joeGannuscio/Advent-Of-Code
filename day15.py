INPUT = [17,1,3,16,19,0]

def part1():
    numbers = {}
    
    for i in range(len(INPUT) - 1):
        numbers[INPUT[i]] = i + 1

    last = INPUT[-1]
    for i in range(len(INPUT), 2020):
        if last in numbers:
            diff = i - numbers[last]
        else:
            diff = 0
        numbers[last] = i
        last = diff

    
    print(last)
    

def part2():
    numbers = {}
    
    for i in range(len(INPUT) - 1):
        numbers[INPUT[i]] = i + 1

    last = INPUT[-1]
    for i in range(len(INPUT), 30000000):
        if last in numbers:
            diff = i - numbers[last]
        else:
            diff = 0
        numbers[last] = i
        last = diff

    
    print(last)


if __name__ == '__main__':
    part1()
    part2()
