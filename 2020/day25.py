def part1():
    pk1 = 14222596
    pk2 = 4057428

    loop1 = 1
    while transform(7, loop1) != pk1:
        loop1 += 1

    loop2 = 1
    while transform(7, loop2) != pk2:
        loop2 += 1

    print(transform(pk1, loop2))


def transform(subject_number, loop_size):
    return pow(subject_number, loop_size, 20201227)


if __name__ == '__main__':
    part1()
