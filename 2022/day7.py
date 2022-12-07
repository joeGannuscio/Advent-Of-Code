def part1(input_path):
    input = read_input_file(input_path)
    root = Directory(name='root')
    cwd = root

    build_file_system(cwd, input)
    root.get_size()

    return


def part2(input_path):
    input = read_input_file(input_path)


    return


def build_file_system(cwd, instructions):
    for instruction in instructions[2:]:
        if 'dir' in instruction:
            name = instruction.split()[1]
            if name not in cwd.subdirectories:
                cwd.subdirectories.append(Directory(name=name, parent=cwd))
                continue

        if '$' in instruction:
            if 'cd ..' in instruction:
                cwd = cwd.parent
            elif 'cd' in instruction:
                cwd = cwd.get_subdirectory(instruction.split()[2])

        if instruction.split()[0].isdigit():
            cwd.files.append(File(name=instruction.split()[1], size=instruction.split()[0]))


def read_input_file(path):
    with open(path) as file:
        return [l.strip() for l in file.readlines()]


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

    def __repr__(self):
        return f'{self.name} is {self.size}'


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.size = 0
        self.subdirectories = []
        self.files = []

    def __repr__(self):
        return f'Directory {self.name} has {len(self.subdirectories)} subdirectories and {len(self.files)} files'

    def get_size(self):
        print(self.name)
        self.size += self._get_total_file_size()
        print(self.size)

        for sd in self.subdirectories:
            sd.get_size()
            self.size += sd.size

        return

    def _get_total_file_size(self):
        size = 0
        for file in self.files:
            size += file.size
        return size

    def get_subdirectory(self, subdirectory_name):
        return next(sd for sd in self.subdirectories if sd.name == subdirectory_name)


if __name__ == '__main__':
    part1('Inputs/day7.txt')
    part2('Inputs/day7.txt')
