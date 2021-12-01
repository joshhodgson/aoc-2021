values = [int(f.strip("\n")) for f in open("input.txt")]
print(
    sum(values[x] > values[x-1] for x in range(1, len(values))),
    sum(sum(values[x-2:x+1]) > sum(values[x-3:x]) for x in range(3, len(values)))
)