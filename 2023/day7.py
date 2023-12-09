from statistics import mode

def part1(input_path):
    hands = read_input_file(input_path)

    hands.sort(key=lambda x: (x.type, (x.hand[0], x.hand[1], x.hand[2], x.hand[3], x.hand[4])))

    score = 0
    for i, hand in enumerate(hands):
        score += (i+1)*hand.bid

    print(score)
    return 


def part2(input_path):
    hands = read_input_file(input_path, True)

    hands.sort(key=lambda x: (x.type, (x.hand[0], x.hand[1], x.hand[2], x.hand[3], x.hand[4])))

    score = 0
    for i, hand in enumerate(hands):
        score += (i+1)*hand.bid

    print(score)
    return 


def read_input_file(path, enable_jokers = False):
    hands = []
    with open(path) as file:
        lines = file.readlines()
        for line in lines:
            s = line.split()
            hands.append(Hand(hand=s[0], bid=int(s[1]), enable_jokers=enable_jokers))



    return hands


class Hand:
    def __init__(self, hand, bid, enable_jokers=False):
        self.enable_jokers = enable_jokers
        self.hand = self._map_hand(hand)
        self.bid = bid
        self.type = self._get_type(self.hand)


    def _map_hand(self, hand):
        if self.enable_jokers:
            vals = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': -1, 'Q': 10, 'K': 11, 'A': 12}
        else:
            vals = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
        new_hand = []
        for c in hand:
            new_hand.append(vals[c])

        return new_hand
    
    def _get_type(self, hand):
        type_hand = hand[:]
        if self.enable_jokers:
            

            # replace jokers with most frequent value
            most = mode(type_hand)

            if most == -1:
                next_most_cnt = 0
                next_most = 0
                for c in type_hand:
                    if c != -1:
                        if type_hand.count(c) >= next_most_cnt:
                            next_most_cnt = type_hand.count(c)
                            next_most = c
                most = next_most
            for i, c in enumerate(type_hand):
                if c == -1:
                    type_hand[i] = most
            unique = len(set(type_hand))
        else:
            unique = len(set(type_hand))

        if unique == 5:
            # all different
            return 0
        
        if unique == 1:
            # all same
            return 6
        
        if unique == 2:
            for card in type_hand:
                 # 4 of a kind
                if type_hand.count(card) == 4:
                    return 5
                # full house
                if type_hand.count(card) == 3:
                    return 4

        if unique == 3:
            for card in type_hand:
                if type_hand.count(card) == 3:
                    # 3 of a kind
                    return 3

            # must be 2 pair
            return 2

        return 1 #one pair last option
    
    def __repr__(self):
        return f'Cards: {self.hand}, Type: {self.type}, Bid: {self.bid}'
    


        


if __name__ == '__main__':
    part1('Inputs/day7.txt')
    part2('Inputs/day7.txt')
