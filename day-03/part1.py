values = [str(f.strip("\n")) for f in open("input.txt")]
max = ""
min = ""
for i in range(len(values[0])):
    ones = 0
    zeros = 0
    for j in values:
        if j[i] == "0":
            zeros += 1
        else:
            ones += 1
    if ones > zeros:
        max = max + "1"
        min = min + "0"
    else:
        min = min + "1"
        max = max + "0"

print(
    int(min, base=2) * int(max, base=2)
)
