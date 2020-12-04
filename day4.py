import re

def part1(input_file):
    passports = read_input_file(input_file)
    valid_count = 0

    for passport in passports:
        if are_valid_fileds_present(passport):
            valid_count += 1

    print(valid_count)

def part2(input_file):
    passports = read_input_file(input_file)

    valid_count = 0

    for passport in passports:

        if not are_valid_fileds_present(passport):
            continue

        if not check_field_validations(passport):
            continue

        valid_count += 1
    
    print(valid_count)


def check_field_validations(passport_fields):
        
    fields = passport_fields.split(' ')
    is_passport_valid = True

    for field in fields:

        parsed_field = field.split(':')
        field_key = parsed_field[0]
        field_value = parsed_field[1]

        if field_key == 'byr':
            if not is_birth_year_valid(field_value):
                is_passport_valid = False
                break
        if field_key == 'iyr':
            if not is_issue_year_valid(field_value):
                is_passport_valid = False
                break
        if field_key == 'eyr':
            if not is_expiration_year_valid(field_value):
                is_passport_valid = False
                break
        if field_key == 'hgt':
            if not is_height_valid(field_value):
                is_passport_valid = False
                break
        if field_key == 'hcl':
            if not is_hair_color_valid(field_value):
                is_passport_valid = False
                break
        if field_key == 'ecl':
            if not is_eye_color_valid(field_value):
                is_passport_valid = False
                break
        if field_key == 'pid':
            if not is_passport_id_valid(field_value):
                is_passport_valid = False
                break

    return is_passport_valid


def are_valid_fileds_present(passport_fields):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for field in required_fields:
        if field in passport_fields:
            continue
        else:
            return False
    return True


def is_birth_year_valid(year):
    if len(year) != 4:
        return False

    if int(year) >= 1920 and int(year) <= 2002:
        return True
    return False

def is_issue_year_valid(year):
    if len(year) != 4:
        return False

    if int(year) >= 2010 and int(year) <= 2020:
        return True
    return False

def is_expiration_year_valid(year):
    if len(year) != 4:
        return False

    if int(year) >= 2020 and int(year) <= 2030:
        return True
    return False

def is_height_valid(height):
    height_val = ''.join(filter(str.isdigit, height))
    if height[-2:] == 'cm':
        if int(height_val) >= 150 and int(height_val) <= 193:
            return True
    elif height[-2:] == 'in':
        if int(height_val) >= 59 and int(height_val) <= 76:
            return True
    else:
        return False
    return False

def is_hair_color_valid(color):

    pattern = re.compile("^#[0-9a-f]{6}$")
    if pattern.match(color):
        return True
    return False
    

def is_eye_color_valid(color):
    valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    if len(color) != 3:
        return False

    if color in valid_colors:
        return True
    return False

def is_passport_id_valid(pid):
    pattern = re.compile("^[0-9]{9}$")
    if pattern.match(pid):
        return True
    return False
        

def read_input_file(path):
    with open(path) as file:
        lines = file.read()
        lines = lines.split('\n\n')
        return [line.replace('\n', ' ') for line in lines]


if __name__ == '__main__':
    part1('Inputs/day4.txt')
    part2('Inputs/day4.txt')