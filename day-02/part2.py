values = [f.strip("\n") for f in open("input.txt")]
horizontal = 0
depth = 0
aim = 0
for i in range(len(values)):
    [action, amount] = values[i].split(" ")
    if action == "forward":
        horizontal += int(amount)
        depth += aim*int(amount)
    if action == "down":
        aim += int(amount)
    if action == "up":
        aim -= int(amount)

print(horizontal*depth)
