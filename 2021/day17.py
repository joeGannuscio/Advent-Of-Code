import re

# The probe's x,y position starts at 0,0. Then, it will follow some trajectory by moving in steps. On each step, these changes occur in the following order:

#     The probe's x position increases by its x velocity.
#     The probe's y position increases by its y velocity.
#     Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
#     Due to gravity, the probe's y velocity decreases by 1.


def part1(input_file):
    input = readInputFile(input_file)
    x_min, x_max = map(int, input[:2])
    y_min, y_max = map(int, input[2:])

    x, y = (0, 0)

    max_heights = []

    for vx0 in range(1, 200):
        for vy0 in range(-200, 200):
            x, y = (0, 0)
            vx, vy = vx0, vy0
            max_height = 0
            for _ in range(500):

                x, y, vx, vy = step(x, y, vx, vy)

                if y > max_height:
                    max_height = y

                if (x_min <= x <= x_max) and (y_min <= y <= y_max):
                    print('hit')
                    max_heights.append(max_height)
                    break

                if x > x_max and y < y_min:
                    print('overshoot')
                    break

    print(max(max_heights))
    print(len(max_heights))
    return


def step(x, y, vx, vy):

    x += vx
    y += vy

    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1
    elif vx == 0:
        vx = 0

    vy -= 1

    return x, y, vx, vy


def part2(input_file):
    input = readInputFile
    return


def readInputFile(path):
    with open(path) as file:
        lines = file.readlines()
        return re.findall(r'-?\d+', lines[0])


if __name__ == '__main__':
    part1('Inputs/day17.txt')
    part2('Inputs/day17.txt')