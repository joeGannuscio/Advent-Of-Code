def part1(input_file):
    inputs = read_input_file(input_file)

    deck_one = [int(c) for c in inputs[0][1].strip().split(' ')]
    deck_two = [int(c) for c in inputs[1][1].strip().split(' ')]

    while len(deck_one) > 0 and len(deck_two) > 0:
        card_one = deck_one.pop(0)
        card_two = deck_two.pop(0)

        if card_one > card_two:
            deck_one.extend([card_one, card_two])
        elif card_two > card_one:
            deck_two.extend([card_two, card_one])
    
    if len(deck_one) == 0:
        print(score(deck_two))
    else:
        print(score(deck_one))
        

def part2(input_file):
    inputs = read_input_file(input_file)

    deck_one = [int(c) for c in inputs[0][1].strip().split(' ')]
    deck_two = [int(c) for c in inputs[1][1].strip().split(' ')]

    print(score(recursive_game(deck_one, deck_two)[1]))

def recursive_game(deck_one, deck_two):
    history = set()

    while len(deck_one) > 0 and len(deck_two) > 0:
        current_state = (tuple(deck_one), tuple(deck_two))
        if current_state in history:
            return ('p1', deck_one)

        history.add(current_state)

        card_one = deck_one.pop(0)
        card_two = deck_two.pop(0)

        if len(deck_one) >= card_one and len(deck_two) >= card_two:
            new_deck_one = list(deck_one)[:card_one]
            new_deck_two = list(deck_two)[:card_two]

            winner, deck = recursive_game(new_deck_one, new_deck_two)
        else:
            if card_one > card_two:
                winner = 'p1'
            else:
                winner = 'p2'

        if winner == 'p1':
            deck_one.extend([card_one, card_two])
        elif winner == 'p2':
            deck_two.extend([card_two, card_one])

    if len(deck_one) == 0:
        return ('p2', deck_two)
    else:
        return ('p1', deck_one)



def score(deck):
    score = 0
    multiplier = 1
    while len(deck) > 0:
        score += multiplier * deck.pop()
        multiplier += 1

    return score


def read_input_file(path):
    with open(path) as file:
        lines = file.read()
        lines = lines.split('\n\n')
        return [line.replace('\n', ' ').lstrip().split(':') for line in lines]


if __name__ == '__main__':
    part1('Inputs/day22.txt')
    part2('Inputs/day22.txt')