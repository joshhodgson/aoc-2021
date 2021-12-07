import re

lines = [str(f.strip("\n")) for f in open("input.txt")]
h, v = 10, 10
for l in lines:
    [x1, y1, x2, y2] = [int(x) for x in re.findall('\d+', l)]
    if x1 > h:
        h = x1+2  # why 2?!?!
    if x2 > h:
        h = x2+2
    if y1 > v:
        v = y1+2
    if y2 > v:
        v = y2+2
print(h, v)
grid = [[0]*v for i in range(h)]

for l in lines:
    print(l)
    [x1, y1, x2, y2] = [int(x) for x in re.findall('\d+', l)]
    blocks = []

    if y1 == y2:
        dy = 0
    elif y1 < y2:
        dy = 1
    else:
        dy = -1
    if x1 == x2:
        dx = 0
    elif x1 < x2:
        dx = 1
    else:
        dx = -1
    blocks.append([x1, y1])
    while not (x1 == x2 and y1 == y2):
        x1 += dx
        y1 += dy
        blocks.append([x1, y1])
    print(blocks)
    for b in blocks:
        grid[b[0]][b[1]] += 1


allnums = sum(grid, [])
print(sum(x > 1 for x in allnums))
