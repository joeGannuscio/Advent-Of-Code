from collections import deque

def part1(input_path):
    input = read_input_file(input_path)

    numbers = []
    for i, number in enumerate(input):
        numbers.append((i, number))

    mixer = list(numbers)

    for i in numbers:
        idx = mixer.index(i)
        mixer.pop(idx)
        new_idx = (i[1] + idx) % len(mixer)
        mixer.insert(new_idx, i)

    for i, n in enumerate(mixer):
        if n[1] == 0:
            zero_idx = i
            break

    gc1k = mixer[(zero_idx + 1000) % len(mixer)]
    gc2k = mixer[(zero_idx + 2000) % len(mixer)]
    gc3k = mixer[(zero_idx + 3000) % len(mixer)]

    print(gc1k[1] + gc2k[1] + gc3k[1])

    return


def part2(input_path):
    input = read_input_file(input_path)

    decryption_key = 811589153

    numbers = []
    for i, number in enumerate(input):
        numbers.append((i, number * decryption_key))

    mixer = list(numbers)

    for _ in range(10):
        for i in numbers:
            idx = mixer.index(i)
            mixer.pop(idx)
            new_idx = (i[1] + idx) % len(mixer)
            mixer.insert(new_idx, i)

    for i, n in enumerate(mixer):
        if n[1] == 0:
            zero_idx = i
            break

    gc1k = mixer[(zero_idx + 1000) % len(mixer)]
    gc2k = mixer[(zero_idx + 2000) % len(mixer)]
    gc3k = mixer[(zero_idx + 3000) % len(mixer)]

    print(gc1k[1] + gc2k[1] + gc3k[1])


    return



def read_input_file(path):
    with open(path) as file:
        return [int(x) for x in file.readlines()]


if __name__ == '__main__':
    part1('Inputs/day20.txt')
    part2('Inputs/day20.txt')
