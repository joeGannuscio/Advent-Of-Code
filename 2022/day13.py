from functools import cmp_to_key


def part1(input_path):
    input = read_input_file(input_path)
    sum = 0
    pair_idx = 0
    for i in range(0, len(input), 2):
        pair_idx += 1
        left = input[i]
        right = input[i+1]

        if is_packet_valid(left, right):
            print(pair_idx)
            sum += pair_idx
    print(sum)
    return


def part2(input_path):
    input = read_input_file(input_path)

    input.extend([[2]])
    input.extend([[6]])
    input.sort(key=cmp_to_key(compare), reverse=True)
    print(input)

    indexes = []
    for i, ipt in enumerate(input):
        if ipt == [2] or ipt == [6]:
            indexes.append(i+1)

    print(indexes[0] * indexes[1])
    return


def is_packet_valid(left, right):
    if compare(left, right) > 0:
        return True
    return False


def compare(left, right):
    # -1 for l > r, 0 for ==, 1 for r > l
    # both int
    if type(left) == int and type(left) == type(right):
        return map_compare_result_to_val(left, right)

    # mixed
    if type(left) != type(right):
        if type(left) == int:
            return compare([left], right)
        else:
            return compare(left, [right])

    # both lists, check each element until one runs out, then compare lengths
    for a, b in zip(left, right):
        check = compare(a, b)
        if check != 0:
            return check

    return map_compare_result_to_val(len(left), len(right))


def map_compare_result_to_val(left, right):
    if left > right:
        return -1
    elif left < right:
        return 1
    else:
        return 0


def read_input_file(path):
    with open(path) as file:
        lines = file.readlines()
        return [eval(l.strip()) for l in lines if l != '\n']


if __name__ == '__main__':
    part1('Inputs/day13.txt')
    part2('Inputs/day13.txt')
