def part1(input_path):
    input = read_input_file(input_path)
    times = input[0]
    dists = input[1]

    win_counts = []

    for i in range(len(input[0])):
        time = times[i]
        dist = dists[i]

        count = 0

        for hold in range(0,time + 1):
            drive_time = time - hold
            speed = hold
            race_dist = speed*drive_time
            if race_dist > dist:
                count +=1
        win_counts.append(count)

    prod = 1
    for w in win_counts:
        prod *= w

    print(prod)


    return 



def part2(input_path):
    input = read_input_file(input_path)
    time = int(''.join(map(str, input[0])))
    dist = int(''.join(map(str, input[1])))

    count = 0

    for hold in range(0,time + 1):
        drive_time = time - hold
        speed = hold
        race_dist = speed*drive_time
        if race_dist > dist:
            count +=1

    print(count)

    return


def read_input_file(path):
    with open(path) as file:
        lines = file.readlines()
        times = list(map(int, lines[0].strip()[5:].split()))
        dist =  list(map(int, lines[1].strip()[9:].split()))




    return (times, dist)


if __name__ == '__main__':
    part1('Inputs/day6.txt')
    part2('Inputs/day6.txt')
