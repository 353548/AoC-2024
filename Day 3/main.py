import re

# Part 1
with open('input.txt', 'r') as f:
    nums = re.findall(r'mul\((\d+),(\d+)\)', f.read().strip())
    nums = [int(mul[0]) * int(mul[1]) for mul in nums]
print(sum(nums))

# Part 2
with open('input.txt', 'r') as f:
    nums = re.findall(r"(?:mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))", f.read().strip())

nums_fix = []

for num in nums:
    if num[2]:
        nums_fix.append(str(num[2]))
    elif num[3]:
        nums_fix.append(str(num[3]))
    else:
        nums_fix.append(int(num[0]) * int(num[1]))

ans = []
do_mul = True
for item in range(len(nums_fix)):
    if nums_fix[item] == "don't()":
        do_mul = False
    elif nums_fix[item] == 'do()':
        do_mul = True
    else:
        if do_mul:
            ans.append(nums_fix[item])
print(sum(ans))