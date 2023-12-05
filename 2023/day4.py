def part1(input_path):
    input = read_input_file(input_path)

    scores = 0

    for card in input:
        winners = set(card[0])
        mine = set(card[1])
        num_matches = len(winners & mine)
        if num_matches > 0:
            scores += get_score(num_matches)

    print(scores)
    return 


def get_score(num_matches):
    return 2**(num_matches-1)


def part2(input_path):
    input = read_input_file(input_path)

    cards = [1] * len(input)

    for i, card in enumerate(input, start=0):
        winners = set(card[0])
        mine = set(card[1])
        num_matches = len(winners & mine)
        for j in range(i + 1, i + 1 + num_matches):
            cards[j] += cards[i]

    print(sum(cards))

    return


def read_input_file(path):
    cards = []
    with open(path) as file:
        lines = file.readlines()
        for line in lines:
            splt_cards = line.strip().split(':')
            nums = splt_cards[1].split('|')
            winners = [int(n) for n in nums[0].strip().split()]
            mine = [int(n) for n in nums[1].strip().split()]

            cards.append((winners, mine))


    return cards


if __name__ == '__main__':
    part1('Inputs/day4.txt')
    part2('Inputs/day4.txt')
