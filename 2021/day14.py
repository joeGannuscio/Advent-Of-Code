from collections import Counter, defaultdict


def part1(input_file):
    input = readInputFile(input_file)
    template = input[0]
    rules = parse_input(input[2:])
    polymer = template
    for _ in range(10):
        polymer = insert(polymer, rules)
    counts = Counter(polymer)
    print(max(counts.values()) - min(counts.values()))
    return


def part2(input_file):
    input = readInputFile(input_file)
    template = input[0]
    rules = parse_input(input[2:])

    pairs = defaultdict(int)
    for i in range(len(template) - 1):
        pairs[template[i:i+2]] += 1

    counts = count_pairs(40, pairs, template, rules)
    print(max(counts.values()) - min(counts.values()))

    return


# thanks lanternfish
def count_pairs(iterations, pairs, template, rules):
    for _ in range(iterations):
        new_pairs = defaultdict(int)
        for pair, count in pairs.items():
            start, end = pair
            inserted = rules[pair]
            new_pairs[start+inserted] += count
            new_pairs[inserted+end] += count
        pairs = new_pairs
    counts = defaultdict(int)
    for pair, count in pairs.items():
        counts[pair[0]] += count
    counts[template[-1]] += 1
    return counts


def insert(polymer, rules):
    updated_polymer = []
    for i in range(len(polymer) - 1):
        pair = polymer[i:i+2]
        inserted = rules[pair]
        updated_polymer.append(pair[:1] + inserted)
    updated_polymer.append(polymer[-1])
    return ''.join([p for p in updated_polymer])


def parse_input(input):
    pairs = dict(s.split(' -> ') for s in input)
    return pairs


def readInputFile(path):
    with open(path) as file:
        lines = file.readlines()
        return [line.strip() for line in lines]


if __name__ == '__main__':
    part1('Inputs/day14.txt')
    part2('Inputs/day14.txt')
