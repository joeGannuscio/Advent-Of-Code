import string
from tokenize import group

def part1(input_path):
    input = read_input_file(input_path)

    sum_priority = 0
    for i in input:
        compartments = split_rucksack(i)
        shared_item = find_shared(compartments[0], compartments[1])
        sum_priority += get_priority(shared_item)

    print(sum_priority)
    return


def part2(input_path):
    input = read_input_file(input_path)
    badges = []

    for i in range(0, len(input), 3):
        badges.append(find_badge(input[i], input[i+1], input[i+2]))

    sum = 0
    for value in badges:
        sum += get_priority(value.pop())

    print(sum)
    return


def split_rucksack(rucksack):
    return [rucksack[:(len(rucksack)//2)], rucksack[(len(rucksack)//2):]]


def find_shared(compartment1, compartment2):
    for item in compartment1:
        if item in compartment2:
            return item

def find_badge(group1, group2, group3):
    return set(group1) & set(group2) & set(group3)

def get_priority(item):
    priority = string.ascii_lowercase.index(item.lower()) + 1
    if item.isupper():
        return priority + 26
    
    return priority



def read_input_file(path):
    with open(path) as file:
        lines = file.readlines()
        return [line.strip() for line in lines]


if __name__ == '__main__':
    part1('Inputs/day3.txt')
    part2('Inputs/day3.txt')
