from collections import defaultdict

# Somehow you can't use f.read()
# twice within one 'with' block.
with open('input.txt', 'r') as f:
    read_rules = [tuple(map(int, i.strip().split('|'))) for i in f.readlines()[:1176]]
with open('input.txt', 'r') as f:
    read_updates = [tuple(map(int, i.strip().split(','))) for i in f.readlines()[1177:]]

rules_order = defaultdict(lambda:[])
for rules in read_rules:
    rules_order[rules[0]].append(rules[1])

def update_check(update):
    # Filter rules present in the current update
    relevant_rules = [(x, y) for x, y in read_rules if x in update and y in update]
    # Map page numbers to their indices in the update
    page_index = {page: idx for idx, page in enumerate(update)}
    for x, y in relevant_rules:
        if page_index[x] >= page_index[y]: # x must come before y
            return False
    return True

# Middle elements of correct updates
updates = [update[len(update) // 2] for update in read_updates if update_check(update)]

print(sum(updates))