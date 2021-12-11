import re

def part1(input_file):
    input = readInputFile(input_file)
    bracket_pairs = {']': '[', '}': '{', ')': '(', '>': '<'}
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}

    score = 0
    for i in input:
        stack = []
        for char in i:
            if char in bracket_pairs.values():
                stack.append(char)
            else:
                if bracket_pairs[char] == stack[-1]:
                    stack.pop()
                else:
                    score += scores[char]
                    break
    print(score)
    return


def part2(input_file):
    input = readInputFile(input_file)
    bracket_pairs = {']': '[', '}': '{', ')': '(', '>': '<'}
    p2_scores = {'(': 1, '[': 2, '{': 3, '<': 4}
    scores = []
    for i in input:
        stack = []
        for char in i:
            if char in bracket_pairs.values():
                stack.append(char)
            else:
                if bracket_pairs[char] == stack[-1]:
                    stack.pop()
                else:
                    break
        else:
            score = 0
            while len(stack) > 0:
                c = stack.pop()
                score *= 5
                score += p2_scores[c]
            scores.append(score)
    print(sorted(scores)[len(scores) // 2])
    return


def readInputFile(path):
    with open(path) as file:
        lines = file.readlines()
        return [line.strip() for line in lines]


if __name__ == '__main__':
    part1('Inputs/day10.txt')
    part2('Inputs/day10.txt')