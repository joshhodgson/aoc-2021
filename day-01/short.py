values = [int(f.strip("\n")) for f in open("example.txt")]
print(sum([1 for x in range(1, len(values)) if values[x] > values[x-1]]))
groupings = [sum(values[x-2:x+1]) for x in range(2, len(values))]
print(sum([1 for x in range(1, len(groupings)) if groupings[x] > groupings[x-1]]))
