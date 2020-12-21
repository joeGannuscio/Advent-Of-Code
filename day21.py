def part1(input_file):
    inputs = read_input_file(input_file)

    allergen_mapping = {}
    ingredients_list = []

    for input in inputs:
        spl = input.split(' (contains ')
        ingredients = (spl[0].split(' '))
        ingredients_list.extend(ingredients)

        allergens = spl[1].replace(')', '').split(', ')
        for allergen in allergens:
            if allergen not in allergen_mapping:
                allergen_mapping[allergen] = set(ingredients)
            else:
                allergen_mapping[allergen].intersection_update(set(ingredients))

    allergen_set = set()

    for allergen in allergen_mapping.values():
        allergen_set.update(allergen)

    non_allergens = set(ingredients_list) - allergen_set

    count = 0

    for ingredient in ingredients_list:
        if ingredient in non_allergens:
            count += 1

    print(count)

def part2(input_file):
    inputs = read_input_file(input_file)

    allergen_mapping = {}
    ingredients_list = []

    for input in inputs:
        spl = input.split(' (contains ')
        ingredients = (spl[0].split(' '))
        ingredients_list.extend(ingredients)

        allergens = spl[1].replace(')', '').split(', ')
        for allergen in allergens:
            if allergen not in allergen_mapping:
                allergen_mapping[allergen] = set(ingredients)
            else:
                allergen_mapping[allergen].intersection_update(set(ingredients))

    allergen_set = set()

    for allergen in allergen_mapping.values():
        allergen_set.update(allergen)

    allergens = {}

    while max([len(v) for v in allergen_mapping.values()]):
        for allergen, ingredients in allergen_mapping.items():
            if len(ingredients) == 1:
                allergens[allergen] = ingredients.pop()
        for allergen in allergen_mapping:
            allergen_mapping[allergen] -= set(allergens.values())

    sorted_allergens = sorted(allergens.items())
    ing = [x[1] for x in sorted_allergens]

    print(','.join(ing))
     

def read_input_file(path):
    with open(path) as file:
        lines = file.readlines()
        return [line.strip() for line in lines]


if __name__ == '__main__':
    part1('Inputs/day21.txt')
    part2('Inputs/day21.txt')
