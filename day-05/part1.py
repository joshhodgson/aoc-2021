import re

lines = [str(f.strip("\n")) for f in open("input.txt")]
h, v = 10, 10
for l in lines:
    [x1, y1, x2, y2] = [int(x) for x in re.findall('\d+', l)]
    if x1 > h:
        h = x1+1
    if x2 > h:
        h = x2+1
    if y1 > v:
        v = y1+1
    if y2 > v:
        v = y2+1
print(h, v)
grid = [[0]*v for i in range(h)]

for l in lines:
    [x1, y1, x2, y2] = [int(x) for x in re.findall('\d+', l)]
    blocks = []
    if y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        while x1 <= x2:
            blocks.append([x1, y1])
            x1 += 1

    else:
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            while y1 <= y2:
                blocks.append([x1, y1])
                y1 += 1
    # print(blocks)
    for b in blocks:
        grid[b[0]][b[1]] += 1

    # break
# print(grid)
allnums = sum(grid, [])
print(sum(x > 1 for x in allnums))
