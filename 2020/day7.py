def part1(input_file):
    rules = read_input_file(input_file)
    rules_dict = parse_rules(rules)

    bags_to_check = {'shiny gold'}
    visited = set()

    while len(bags_to_check) > 0:
        current_bag = bags_to_check.pop()
        bags = [color for color, contents in rules_dict.items() if current_bag in contents.keys()]
        bags_to_check.update(bags)
        visited.update(bags)
    print(len(visited))


def part2(input_file):
    rules = read_input_file(input_file)
    rules_dict = parse_rules(rules)
    bags_count = 0
    bags_to_process = ['shiny gold']
    while len(bags_to_process) > 0:
        process = bags_to_process.pop()
        contents = rules_dict[process]
        for color, number_of_bags in contents.items():
            bags_count += number_of_bags
            bags_to_process.extend([color] * number_of_bags)

    print(bags_count)
 

def parse_rules(rules):
    rule_dict = {}

    for rule in rules:
            bag = rule.split(' bags contain ')
            contents = bag[1].replace('.', '')
            contents = contents.split(', ')
            contents_dict = {}

            if 'no other bags' in contents:
                rule_dict[bag[0]] = {}
            else:
                for con in contents:
                    con = con.replace('bags', '')
                    con = con.replace('bag', '')
                    con = con.strip()
                    parsed = con.split(' ', 1)
                    contents_dict[parsed[1]] = int(parsed[0])
                
                rule_dict[bag[0]] = contents_dict

    return rule_dict            


def read_input_file(path):
    with open(path) as file:
        lines = file.readlines()
        return [line.strip() for line in lines]


if __name__ == '__main__':
    part1('Inputs/day7.txt')
    part2('Inputs/day7.txt')
