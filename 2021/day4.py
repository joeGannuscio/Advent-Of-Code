def part1(input_file):
    input = readInputFile(input_file)
    call = [int(x) for x in input[0].split(',')]

    boards = build_boards(input[1:])

    #play the game
    for num in call:
        for board in boards:
            board.process_number_called(num)
            if board.is_winner():
                print(board.score(num))
                return

    return

def part2(input_file):
    input = readInputFile(input_file)
    call = [int(x) for x in input[0].split(',')]

    boards = build_boards(input[1:])

    #play the game
    score = 0
    for num in call:
        for board in boards:
            board.process_number_called(num)
            if board.is_winner() and board.has_won == False:
                board.has_won = True
                score = board.score(num)

    print(score)
    return

def readInputFile(path):
    with open(path) as file:
        lines = file.readlines()
        return [line.strip() for line in lines]

def build_boards(input):
    row_count = 0
    data = []
    boards = []
    for row in input[1:]:
        if row == '':
            data.clear()
            row_count = 0
            continue

        if row_count != 5:
            data.append([int(x) for x in row.split()])
            row_count += 1

        if row_count == 5:
            boards.append(Board(data))
    return boards

class Board:

    def __init__(self, data):
        self.win_options = []
        self.has_won = False
        self.generate_win_options(data)

    def generate_win_options(self, data):
        # rows
        for row in data:
            self.win_options.append(row)

        for i in range(0, 5):
            col = []
            for row in data:
                col.append(row[i])
            self.win_options.append(col)

    def process_number_called(self, number):
        for opt in self.win_options:
            if number in opt:
                opt.remove(number)

    def is_winner(self):
        for opt in self.win_options:
            if len(opt) == 0:
                return True    
        return False
    
    def score(self, last_called):
        score = 0
        for row in self.win_options[:5]:
            score += sum(row)    
        return score * last_called


if __name__ == '__main__':
    part1('Inputs/day4.txt')
    part2('Inputs/day4.txt')