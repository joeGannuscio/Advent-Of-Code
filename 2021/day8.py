from itertools import permutations


def part1(input_file):
    input = readInputFile(input_file)
    outputs = []
    for i in input:
        outputs.append(i[1].strip().split(' '))

    total = 0
    for o in outputs:
        for v in o:
            if len(v) == 2 or len(v) == 3 or len(v) == 4 or len(v) == 7:
                total += 1

    print(total)
    return


def part2(input_file):
    input = readInputFile(input_file)
    signal_patterns = []
    outputs = []

    # make a tempalte for each digit
    # map the template value to a permutation of the letters
    # apply the mapped value to the signal pattern
    # check each possibility against the template until you get a match
    # figure out the outputs digits from the now known digits

    templates = {'abcefg': '0', 'cf': '1', 'acdeg': '2', 'acdfg': '3', 'bcdf': '4', 'abdfg':'5', 'abdefg': '6', 'acf': '7', 'abcdefg': '8', 'abcdfg': '9'}

    sum = 0
    for line in input:
        signal_patterns = line[0].split()
        outputs = line[1].split()

        for p in permutations(list('abcdefg')):
            mapper = get_mapper(p)

            matches = []
            for pat in signal_patterns:
                mapped_digit = ''.join(sorted(mapper[x] for x in pat))

                if mapped_digit in templates.keys():
                    matches.append(mapped_digit)

            if len(matches) == 10:
                output_digits = ''
                for out in outputs:
                    mapped_out = ''.join(sorted(mapper[x] for x in out))
                    output_digits += templates[mapped_out]
                sum += int(output_digits)
                break
    print(sum)
    return


def get_mapper(perm):
    mapper = {}
    for templ_val, pat_val in zip('abcdefg', perm):
        mapper[templ_val] = pat_val
    return mapper


def readInputFile(path):
    with open(path) as file:
        lines = file.readlines()
        return [line.strip().split('|') for line in lines]


if __name__ == '__main__':
    part1('Inputs/day8.txt')
    part2('Inputs/day8.txt')
