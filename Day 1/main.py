with open('input.txt', 'r') as f:
    pairs = [list(map(int, numbers.strip().split())) for numbers in f.readlines()]

left_side = []
right_side = []

for pair in pairs:
    left_side.append(pair[0])
    right_side.append(pair[1])

left_side = sorted(left_side)
right_side = sorted(right_side)

difference = []

for index in range(len(pairs)):
    apart = abs(left_side[index] - right_side[index])
    difference.append(apart)

# Part 1 answer
print(sum(difference))

# Part 2 answer
similarity = []
for number in left_side:
    similarity.append(number * right_side.count(number))
print(sum(similarity))