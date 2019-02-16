from functools import (reduce)
from itertools import (starmap)


def maxPathSum(rows):
    return reduce(
        lambda xs, ys: list(starmap(
            lambda a, b, c: a + max(b, c),
            zip(ys, xs, xs[1:])
        )),
        reversed(rows[:-1]), rows[-1]
    )[0]

with open('zadanie_4_triangle_big.txt', 'r') as f:
	lists = f.readlines()

int_triangle=[]
for line in lists:
	new_list=[]
	string_list = line.split(' ')
	for value in string_list:
		try:
			new_list.append(int(value))
		except:
			pass
	int_triangle.append(new_list)

print(maxPathSum(int_triangle))


