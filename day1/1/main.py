"""In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020
what do you get if you multiply them together?

Your puzzle answer was 793524."""

# O(n)


def fun(entries):
    resultSet = set()
    for x in entries:
        rest = 2020 - x
        if rest in resultSet:
            return rest * x
        else:
            resultSet.add(x)


inputfile = open('input.txt', 'r')
lines = inputfile.readlines()
entries = [int(x.strip()) for x in lines]

result = fun(entries)
print("Result fun: %d" % result)
