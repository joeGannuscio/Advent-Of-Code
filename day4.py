def main():
    inputLow = 109165
    inputHigh = 576723
    part1(inputLow, inputHigh)

def part1(min, max):
    count = 0
    for val in range(min, max):
        if(checkValue(val)):
            count += 1
    print(count)

def part2(min, max):
    count = 0
    for val in range(min, max):
        if(checkValue(val)):
            count += 1
    print(count)

def checkValue(val):

    numbers = [int(num) for num in str(val)]
    repeatFlag = False
    previousNumber = 0

    for number in numbers:
        if (numbers.count(number) == 2):
            repeatFlag = True
        if (number < previousNumber):
            return False
        previousNumber = number    
    return repeatFlag

if __name__ == '__main__':
    main()