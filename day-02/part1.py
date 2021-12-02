values = [f.strip("\n") for f in open("input.txt")]
horizontal = 0
depth = 0
for i in range(len(values)):
    [action, amount] = values[i].split(" ")
    if action == "forward":
        horizontal += int(amount)
    if action == "down":
        depth += int(amount)
    if action == "up":
        depth -= int(amount)

print(horizontal*depth)
