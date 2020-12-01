"""he three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

Your puzzle answer was 61515678."""
# O(n^3)


def fun(entries):
    size = len(entries)
    for i in range(size):
        for j in range(i + 1, size):
            for k in range(j + 1, size):
                if entries[i] + entries[j] + entries[k] == 2020:
                    return entries[i] * entries[j] * entries[k]


inputfile = open('input.txt', 'r')
lines = inputfile.readlines()
entries = [int(x.strip()) for x in lines]

result = fun(entries)
print("Result fun: %d" % result)
