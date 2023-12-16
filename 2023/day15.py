def part1(input_path):
    input = read_input_file(input_path)

    init = input.split(',')
    sum = 0
    for i in init:
        sum += calculate_hash(i)

    print(sum)


    return 


def part2(input_path):
    input = read_input_file(input_path)

    init = input.split(',')
    
    boxes = [dict() for _ in range(256)]

    for i in init:
        if '=' in i:
            label, focal = i.split('=')
            boxes[calculate_hash(label)][label] = int(focal)
        else:
            label, focal = i.split('-')
            boxes[calculate_hash(label)].pop(label, None)

    score = 0
    for i, box in enumerate(boxes):
        box_score = i + 1
        for j, f in enumerate(box.values()):
            score += box_score * (j+1) * f


    print(score)
    return 


def calculate_hash(input):

    current_value = 0

    for c in input:
        ascii_code = ord(c)
        current_value += ascii_code
        current_value *= 17
        current_value = current_value % 256

    return current_value


def read_input_file(path):
    with open(path) as file:
        input = file.read()

    return input


if __name__ == '__main__':
    part1('Inputs/day15.txt')
    part2('Inputs/day15.txt')
