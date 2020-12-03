inputfile = open('01_input.txt', 'r')
lines = inputfile.readlines()
entries = [int(x.strip()) for x in lines]

"""In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020
what do you get if you multiply them together?

Your puzzle answer was 793524."""
# O(n)


def part1(entries):
    resultSet = set()
    for x in entries:
        rest = 2020 - x
        if rest in resultSet:
            return rest * x
        else:
            resultSet.add(x)


result = part1(entries)
print("Result part1: %d" % result)

"""he three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

Your puzzle answer was 61515678."""
# O(n^3)


def part2(entries):
    size = len(entries)
    for i in range(size):
        for j in range(i + 1, size):
            for k in range(j + 1, size):
                if entries[i] + entries[j] + entries[k] == 2020:
                    return entries[i] * entries[j] * entries[k]


result = part2(entries)
print("Result part2: %d" % result)
