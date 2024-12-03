import re

# Part 1
with open('input.txt', 'r') as f:
    nums = re.findall(r'mul\((\d+),(\d+)\)', f.read().strip())
    nums = [int(mul[0]) * int(mul[1]) for mul in nums]
print(sum(nums))

# Part 2
with open('input.txt', 'r') as f:
    matches = re.findall(
        r"(?:mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))",
        f.read().strip()
        )

items = [
    int(m[0]) * int(m[1]) if m[0] and m[1] else m[2] or m[3]
    for m in matches
]

ans = []
do_mul = True

for item in items:
    if item == "don't()":
        do_mul = False
    elif item == 'do()':
        do_mul = True
    else:
        if do_mul:
            ans.append(item)

print(sum(ans))