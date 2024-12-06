with open('input.txt', 'r') as f:
    puzzle = [list(i.strip()) for i in f.readlines()]

class Guard:
    def __init__(self, y, x):
        self.y_pos = y
        self.x_pos = x
        self.status = True
        self.char = puzzle[y][x]

    def get_pos(self):
        return (self.y_pos, self.x_pos)
    
    def in_map(self):
        if self.status:
            if self.y_pos in range(0, y_dim):
                if self.x_pos in range(0, x_dim):
                    return True 
        return False
    
    def do_move(self):
        chars = {'^': (-1 ,0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
        dy, dx = chars[self.char]
        try:
            if puzzle[self.y_pos + dy][self.x_pos + dx] == '#':
                rotation = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
                self.char = rotation[self.char]
            else:
                puzzle[self.y_pos][self.x_pos] = 'X'
                self.y_pos += dy
                self.x_pos += dx
                puzzle[self.y_pos][self.x_pos] = self.char
        except IndexError:
            puzzle[self.y_pos][self.x_pos] = 'X'
            self.status = False


# Map dimensions
y_dim = len(puzzle)
x_dim = len(puzzle[0])

# Gurad starting location
for y in range(y_dim):
    for x in range(x_dim):
        if puzzle[y][x] == '^':
            guard = Guard(y, x) # Initialize guard at her location

# Let's get moving
while guard.in_map():
    guard.do_move()

# Show updated map
for row in puzzle:
    print(''.join(row))

x_count = sum(row.count('X') for row in puzzle)
print("X's: ", x_count)