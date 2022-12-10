def part1(input_path):
    input = read_input_file(input_path)

    visible_count = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if is_tree_visible(i, j, input):
                visible_count += 1

    print(visible_count)
    return


def part2(input_path):
    input = read_input_file(input_path)

    scenic_scores = []
    for i in range(len(input)):
        for j in range(len(input[0])):
            scenic_scores.append(get_scenic_score(i, j, input))

    print(max(scenic_scores))

    return


def get_scenic_score(tree_y, tree_x, forest):
    # check if edge
    if tree_y == 0 or tree_x == 0 or tree_y == len(forest) - 1 or tree_x == len(forest[0]) - 1:
        return 0
    current_height = forest[tree_y][tree_x]
    # check left
    left = 0
    for x in range(tree_x - 1, -1, -1):
        tree = forest[tree_y][x]
        if current_height <= tree:
            left += 1
            break
        else:
            left += 1

    # check right
    right = 0
    for x in range(tree_x + 1, len(forest[0])):
        tree = forest[tree_y][x]
        if current_height <= tree:
            right += 1
            break
        else:
            right += 1

    # check above
    above = 0
    for y in range(tree_y - 1, -1, -1):
        tree = forest[y][tree_x]
        if current_height <= tree:
            above += 1
            break
        else:
            above += 1

    # check below
    below = 0
    for y in range(tree_y + 1, len(forest)):
        tree = forest[y][tree_x]
        if current_height <= tree:
            below += 1
            break
        else:
            below += 1

    return left * right * above * below


def is_tree_visible(tree_y, tree_x, forest):
    # check if edge
    if tree_y == 0 or tree_x == 0 or tree_y == len(forest) - 1 or tree_x == len(forest[0]) - 1:
        return True
    current_height = forest[tree_y][tree_x]
    # check left
    left = []
    for x in range(0, tree_x):
        left.append(forest[tree_y][x])
    if current_height > max(left):
        return True
    # check right
    right = []
    for x in range(tree_x + 1, len(forest)):
        right.append(forest[tree_y][x])
    if current_height > max(right):
        return True
    # check above
    above = []
    for y in range(0, tree_y):
        above.append(forest[y][tree_x])
    if current_height > max(above):
        return True
    # check below
    below = []
    for y in range(tree_y + 1, len(forest)):
        below.append(forest[y][tree_x])
    if current_height > max(below):
        return True
    return False





def get_forest_grid(tree_heights):
    forest = {}
    for i in range(len(tree_heights)):
        for j in range(len(tree_heights[0])):
            forest[(i, j)] = tree_heights[i][j]

    return forest




def read_input_file(path):
    with open(path) as file:
        lines = file.readlines()
        raw_input = [line.strip() for line in lines]
        return [[int(c) for c in x] for x in raw_input]



if __name__ == '__main__':
    part1('Inputs/day8.txt')
    part2('Inputs/day8.txt')
