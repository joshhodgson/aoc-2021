values = [int(f.strip("\n")) for f in open("example.txt")]
print(sum([1 for x in range(1, len(values)) if values[x] > values[x-1]]))
print(sum([1 for x in range(3, len(values)) if sum(values[x-2:x+1]) > sum(values[x-3:x])]))
