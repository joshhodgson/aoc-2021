lines = [str(f.strip("\n")) for f in open("input.txt")]
values = [int(v) for v in lines[0].split(",")]
print(values)
smallest = 100000000
for x in range(max(values)):
    fuel = sum(abs(x-v) for v in values)
    if fuel < smallest:
        smallest = fuel
print(smallest)
