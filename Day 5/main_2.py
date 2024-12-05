from collections import defaultdict, deque

# Read rules and updates from the file
with open('input.txt', 'r') as f:
    read_rules = [tuple(map(int, i.strip().split('|'))) for i in f.readlines()[:1176]]
with open('input.txt', 'r') as f:
    read_updates = [list(map(int, i.strip().split(','))) for i in f.readlines()[1177:]]

def update_check(update, rules):
    """
    Check if the given update respects the rules.
    """
    # Filter rules present in the current update
    relevant_rules = [(x, y) for x, y in rules if x in update and y in update]
    # Map page numbers to their indices in the update
    page_index = {page: idx for idx, page in enumerate(update)}
    # Verify if all rules are satisfied
    for x, y in relevant_rules:
        if page_index[x] >= page_index[y]:  # x must come before y
            return False
    return True

def fix_update(update, rules):
    """
    Reorder the update using topological sorting to satisfy the rules.
    """
    # Filter relevant rules
    relevant_rules = [(x, y) for x, y in rules if x in update and y in update]
    
    # Build a graph for topological sort
    graph = defaultdict(list)
    indegree = defaultdict(int)
    
    for x, y in relevant_rules:
        graph[x].append(y)
        indegree[y] += 1
        indegree[x]  # Ensure x exists in the indegree dictionary

    # Topological sort using Kahn's algorithm
    queue = deque([node for node in update if indegree[node] == 0])
    sorted_update = []

    while queue:
        current = queue.popleft()
        sorted_update.append(current)
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # If all nodes are sorted, return sorted_update; otherwise, return the original update
    return sorted_update if len(sorted_update) == len(update) else update

# Check and optionally fix updates
fixed_updates = [fix_update(update, read_rules)[len(update)//2] for update in read_updates if not update_check(update, read_rules)]
print(sum(fixed_updates))