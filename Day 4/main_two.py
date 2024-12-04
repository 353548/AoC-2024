with open('input.txt', 'r') as f:
    text = [i.strip() for i in f.readlines()]

def search(file):
    rows = len(file)
    columns = len(file[0])
    xmas = 0
    for y in range(rows):
        for x in range(columns):
            if file[y][x] == 'A':
                try:
                    if file[y+1][x-1] == 'M' and file[y+1][x+1] == 'M':
                        if file[y-1][x-1] == 'S' and file[y-1][x+1] == 'S':
                            if y+1 < rows and y-1 >= 0 and x-1 >= 0 and x+1 < columns:
                                xmas +=1
                except IndexError: pass

                try:
                    if file[y+1][x-1] == 'S' and file[y+1][x+1] == 'S':
                        if file[y-1][x-1] == 'M' and file[y-1][x+1] == 'M':
                            if y+1 < rows and y-1 >= 0 and x-1 >= 0 and x+1 < columns:
                                xmas += 1
                except IndexError: pass
                try:
                    if file[y+1][x-1] == 'M' and file[y+1][x+1] == 'S':
                        if file[y-1][x-1] == 'M' and file[y-1][x+1] == 'S':
                            if y+1 < rows and y-1 >= 0 and x-1 >= 0 and x+1 < columns:
                                xmas += 1
                except IndexError: pass
                try:
                    if file[y+1][x-1] == 'S' and file[y+1][x+1] == 'M':
                        if file[y-1][x-1] == 'S' and file[y-1][x+1] == 'M':
                            if y+1 < rows and y-1 >= 0 and x-1 >= 0 and x+1 < columns:
                                xmas += 1
                except IndexError: pass
    return xmas


x = search(text)
print(x)