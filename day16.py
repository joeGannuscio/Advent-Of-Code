def part1(input_file):
    inputs = read_input_file(input_file)
    rules, ticket, nearby_tickets = parse_input(inputs)


    parsed_rules = [rule.split(':') for rule in rules]
    allowed_values = []
    
    for rule in parsed_rules:
        parts = rule[1].strip().split(' ')
        for part in parts:
            if part == 'or':
                continue
            spl = part.split('-')
            mini = int(spl[0])
            maxi = int(spl[1])

            for i in range(mini, maxi + 1):
                if i not in allowed_values:
                    allowed_values.append(i)

    nearby_tickets = ','.join(nearby_tickets)
    tickets_to_check = nearby_tickets.split(',')
    tickets_to_check = [int(ticket) for ticket in tickets_to_check[1:]]

    sum_of_invalid = 0

    for ticket in tickets_to_check:
        if ticket not in allowed_values:
            print(ticket)
            sum_of_invalid += ticket
    print(sum_of_invalid)


def parse_input(input):
    your_ticket_flag = False
    nearby_ticket_flag = False
    rules = []
    your_ticket = []
    nearby_tickets = []
    for line in input:
        if line == '':
            continue

        if 'your ticket' in line:
            your_ticket_flag = True
            continue

        if 'nearby tickets' in line:
            nearby_ticket_flag = True
            continue

        if not your_ticket_flag and not nearby_ticket_flag:
            rules.append(line)

        if your_ticket_flag and not nearby_ticket_flag:
            your_ticket.append(line)

        if nearby_ticket_flag:
            nearby_tickets.append(line)

    return (rules, your_ticket, nearby_tickets)


        

def part2(input_file):
    print('part2')


def read_input_file(path):
    with open(path) as file:
        lines = file.read()
        return lines.split('\n')

if __name__ == '__main__':
    part1('Inputs/day16.txt')
    part2('Inputs/day16.txt')
