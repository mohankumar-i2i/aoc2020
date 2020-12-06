import string

with open('06_input.txt') as f:
    lines = [l.rstrip('\n') for l in f.read().split('\n\n')]

ct = 0
for line in lines:
    ct += len(set(c for c in line if 'a' <= c <= 'z'))
print("Result solution1: %d" % ct)

ct = 0
for line in lines:
    alls = set(string.ascii_lowercase)
    for ll in line.split('\n'):
        alls &= set(c for c in ll if 'a' <= c <= 'z')
    ct += len(alls)
print("Result solution2: %d" % ct)
