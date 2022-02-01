lines = [str(f.strip("\n")) for f in open("input.txt")]
total = 0
for l in lines:
    value = l.split("|")[1].strip().split(" ")
    print(value)
    total += len([v for v in value if len(v) in [2, 3, 4, 7]])
print(total)
