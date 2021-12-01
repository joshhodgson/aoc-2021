values = [int(f.strip("\n")) for f in open("input.txt")]
total = 0
for i in range(1, len(values)):
    if values[i] > values[i-1]:
        total += 1
print(total)
