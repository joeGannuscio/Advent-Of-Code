def part1(input_path):
    input = read_input_file(input_path)

    parts = []

    for y in range(len(input)):
        num_string = ''
        is_part = False
        is_number = False
        for x in range(len(input[0])):
            if input[y][x].isdigit():
                is_number = True
                num_string += input[y][x]
                if not is_part:
                    is_part = check_neighbors(input, y, x)

            else:
                if is_number and is_part:
                    parts.append(num_string)
                num_string = ''
                is_part = False
                is_number = False

            if is_number and is_part and x == len(input[0]) - 1:
                parts.append(num_string)

    print(sum(map(int, parts)))



    return 


def check_neighbors(grid, y, x):
    moves = [(0,1), (0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
    max_x = len(grid[0])
    max_y = len(grid)

    for move in moves:
        neighbor = (y + move[0], x + move[1])
        if 0 <= neighbor[0] < max_y and 0 <= neighbor[1] < max_x:
            val = grid[neighbor[0]][neighbor[1]]
            
            if not val.isdigit() and val.strip() != '':
                return True

    return False



        



def part2(input_path):
    input = read_input_file(input_path)

    return


def read_input_file(path):
    map=[]
    with open(path) as file:
        lines = file.readlines()
        for line in lines:
            row = []
            for c in line.strip():
                if c == '.':
                    row.append('')
                else:
                    row.append(c)
            map.append(row)
    return map


if __name__ == '__main__':
    part1('Inputs/day3.txt')
    part2('Inputs/day3.txt')
