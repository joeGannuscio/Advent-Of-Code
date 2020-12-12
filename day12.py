def part1(input_file):
    inputs = read_input_file(input_file)

    # > facing east to start start at 0, 0
    heading = 'E'
    headings = ['N', 'E', 'S', 'W']
    ship_x = 0
    ship_y = 0
    for input in inputs:
        direction = input[0]
        distance = int(input[1:])

        if direction == 'E':
            ship_x += distance
        elif direction == 'W':
            ship_x -= distance
        elif direction == 'N':
            ship_y += distance
        elif direction == 'S':
            ship_y -= distance

        elif direction == 'F':
            if heading == 'E':
                ship_x += distance
            elif heading == 'W':
                ship_x -= distance
            elif heading == 'N':
                ship_y += distance
            elif heading == 'S':
                ship_y -= distance
        
        elif direction == 'R':
            num_of_turns = distance // 90

            index = headings.index(heading)
            
            if index + num_of_turns > len(headings) - 1:
                heading = headings[(index + num_of_turns) - 4]
            else:
                heading = headings[index + num_of_turns]


        elif direction == 'L':
            num_of_turns = distance // 90

            index = headings.index(heading)
            
            if index - num_of_turns < 0:
                heading = headings[(index - num_of_turns) + 4]
            else:
                heading = headings[index - num_of_turns]
            

    print(abs(ship_x)+ abs(ship_y))


def part2(input_file):
    inputs = read_input_file(input_file)

    # > facing east to start start at 0, 0
    ship_x = 0
    ship_y = 0
    waypoint_x = 10
    waypoint_y = 1
    for input in inputs:
        direction = input[0]
        distance = int(input[1:])

        if direction == 'E':
            waypoint_x += distance
        elif direction == 'W':
            waypoint_x -= distance
        elif direction == 'N':
            waypoint_y += distance
        elif direction == 'S':
            waypoint_y -= distance

        elif direction == 'F':
            ship_x += distance * waypoint_x
            ship_y += distance * waypoint_y
        
        elif direction == 'R':
            for _ in range(distance//90):
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x
                
        elif direction == 'L':
            for _ in range(distance//90):
                waypoint_x, waypoint_y = -waypoint_y, waypoint_x

    print(abs(ship_x)+ abs(ship_y))



def read_input_file(path):
    with open(path) as file:
        lines = file.readlines()
        return [line.strip() for line in lines]


if __name__ == '__main__':
    part1('Inputs/day12.txt')
    part2('Inputs/day12.txt')
    