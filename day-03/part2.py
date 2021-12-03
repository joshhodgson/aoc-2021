values = [str(f.strip("\n")) for f in open("input.txt")]

carbon = [v for v in values]
oxygen = [v for v in values]

for i in range(len(values[0])):

    if len(oxygen) > 1:
        ones = 0
        zeros = 0
        for j in oxygen:
            if j[i] == "0":
                zeros += 1
            else:
                ones += 1
        if ones >= zeros:
            oxygen = [o for o in oxygen if o[i] == "1"]
        else:
            oxygen = [o for o in oxygen if o[i] == "0"]

    if len(carbon) > 1:
        ones = 0
        zeros = 0
        for j in carbon:
            if j[i] == "0":
                zeros += 1
            else:
                ones += 1
        if ones >= zeros:
            carbon = [c for c in carbon if c[i] == "0"]
        else:
            carbon = [c for c in carbon if c[i] == "1"]

print(
    int(oxygen[0], base=2) * int(carbon[0], base=2)
)
