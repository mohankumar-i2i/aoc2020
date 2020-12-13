from itertools import count
from sympy.ntheory.modular import solve_congruence
from aocd import get_data
data = get_data(day=13)
ls = data.split("\n")

earliest = int(ls[0])
bus_times = [(-i, int(x)) for i, x in enumerate(ls[1].split(',')) if x != 'x']
_, busses = zip(*bus_times)

# Part one
print(next((time - earliest)*bus
           for time in count(earliest) for bus in busses
           if time % bus == 0))

# Part two
print(solve_congruence(*bus_times)[0])
