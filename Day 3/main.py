import re

with open('input.txt', 'r') as f:
    nums = re.findall(r'mul\((\d+),(\d+)\)', f.read().strip())
    nums = [int(mul[0]) * int(mul[1]) for mul in nums]

print(sum(nums))