from itertools import combinations, permutations, combinations_with_replacement as cwr
from itertools import permutations, product

puzzles = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
puzzles = {int(puzzle.split(':')[0]): list(map(int, ' '.join(puzzle.split(':')[1:]).strip().split())) for puzzle in puzzles.strip().splitlines()}

results = 0

for left in puzzles.keys():
    items = puzzles[left]
    operations = product('+*', repeat=len(items) - 1)

    tmpres = []
    for operaton in operations:
        tmpitems = items[::]
        num = tmpitems[0]
        tmpitems.pop(0)
        for sign in operaton:
            if sign == '+':
                num += tmpitems.pop(0)
            elif sign == '*':
                num *= tmpitems.pop(0)
        tmpres.append(num)
    print(tmpres)
    if left in tmpres:
        results += 1
print(results)