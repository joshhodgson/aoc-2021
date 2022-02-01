lines = [str(f.strip("\n")) for f in open("input.txt")]
values = [int(v) for v in lines[0].split(",")]
print(values)
states = [0]*10
for v in values:
    states[v] += 1
print(states)
for tick in range(256):
    resets = 0
    new = 0
    for (i, v) in enumerate(states):
        print(i, v)
        if i == 0:
            resets = v
            new = v
            continue
        states[i-1] = v
    states[6] += resets
    states[8] += new
    print(states)
print(sum(states))
