def part1(input_path):
    input = read_input_file(input_path)
    root = Directory(name='root')
    cwd = root

    build_file_system(cwd, input)

    sizes = []

    def get_directory_sizes(directory):
        sizes.append(directory.get_size())
        for sd in directory.subdirectories:
            get_directory_sizes(sd)

    get_directory_sizes(root)

    print(sum([s for s in sizes if s <= 100000]))

    return


def part2(input_path):
    input = read_input_file(input_path)
    root = Directory(name='root')
    cwd = root

    build_file_system(cwd, input)

    total_space = 70000000
    required_space = 30000000
    used_space = root.get_size()

    delete_size = required_space - (total_space-used_space)

    sizes = []

    def get_directory_sizes(directory):
        sizes.append(directory.get_size())
        for sd in directory.subdirectories:
            get_directory_sizes(sd)

    get_directory_sizes(root)
    sizes = sorted(sizes)
    for s in sizes:
        if s >= delete_size:
            print(s)
            return


def build_file_system(cwd, instructions):
    for instruction in instructions[2:]:
        if 'dir' in instruction:
            name = instruction.split()[1]
            cwd.add_subdirectory(name)
        elif '$' in instruction:
            if 'cd ..' in instruction:
                cwd = cwd.parent
            elif 'cd' in instruction:
                cwd = cwd.get_subdirectory(instruction.split()[2])

        elif instruction.split()[0].isdigit():
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
        self.subdirectories = []
        self.files = []

    def __repr__(self):
        return f'Directory {self.name} has {len(self.subdirectories)} subdirectories and {len(self.files)} files'

    def get_size(self):
        size = 0
        size += self._get_total_file_size()
        for sd in self.subdirectories:
            size += sd.get_size()
        return size

    def add_subdirectory(self, name):
        if name not in self.get_subdirectory_names():
            self.subdirectories.append(Directory(name, self))

    def get_subdirectory_names(self):
        return [n.name for n in self.subdirectories]

    def _get_total_file_size(self):
        size = 0
        for file in self.files:
            size += file.size
        return size

    def get_subdirectory(self, subdirectory_name):
        for sd in self.subdirectories:
            if sd.name == subdirectory_name:
                return sd
        return None


if __name__ == '__main__':
    part1('Inputs/day7.txt')
    part2('Inputs/day7.txt')
