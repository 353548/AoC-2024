with open('input.txt', 'r') as f:
    text = [i.strip() for i in f.readlines()]

"""
NOTE TO SELF:
If you use negative values as list indexes Python will
access them anyway. This really made it hard to find
what is wrong with today's code.
"""

def search(file):
    rows = len(file)
    columns = len(file[0])
    xmas = 0
    for y in range(rows):
        for x in range(columns):
            if file[y][x] == 'X':
                try:
                    if y-3 >= 0 and x+3 < columns and file[y-1][x+1] == 'M' and file[y-2][x+2] == 'A' and file[y-3][x+3] == 'S':
                                xmas += 1
                except IndexError: pass

                try:
                    if x+3 < columns and file[y][x+1] == 'M' and file[y][x+2] == 'A' and file[y][x+3] == 'S':
                                xmas += 1
                except IndexError: pass

                try:
                    if y+3 < rows and x+3 < columns and file[y+1][x+1] == 'M' and file[y+2][x+2] == 'A' and file[y+3][x+3] == 'S':
                                xmas += 1
                except IndexError: pass

                try:
                    if y-3 >= 0 and file[y-1][x] == 'M' and file[y-2][x] == 'A' and file[y-3][x] == 'S':
                                xmas += 1
                except IndexError: pass

                try:
                    if y+3 < rows and file[y+1][x] == 'M' and file[y+2][x] == 'A' and file[y+3][x] == 'S':
                                xmas += 1
                except IndexError: pass

                try:
                    if y-3 >= 0 and x-3 >=0 and file[y-1][x-1] == 'M' and file[y-2][x-2] == 'A' and file[y-3][x-3] == 'S':
                                xmas += 1
                except IndexError: pass

                try:
                    if x-3 >= 0 and file[y][x-1] == 'M' and file[y][x-2] == 'A' and file[y][x-3] == 'S':
                                xmas += 1
                except IndexError: pass

                try:
                    if y+3 < rows and x-3 >=0 and file[y+1][x-1] == 'M' and file[y+2][x-2] == 'A' and file[y+3][x-3] == 'S':
                                xmas += 1
                except IndexError: pass
    return xmas

x = search(text)
print(x)