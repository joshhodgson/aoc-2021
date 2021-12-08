lines = [str(f.strip("\n")) for f in open("input.txt")]


def decodeLine(line):
    code = line.split("|")[0].strip().split(" ")
    order = [""]*10
    order[1] = [c for c in code if len(c) == 2][0]
    order[7] = [c for c in code if len(c) == 3][0]
    order[4] = [c for c in code if len(c) == 4][0]
    order[8] = [c for c in code if len(c) == 7][0]

    nineminusg = "".join(set(order[4]+order[7]))
    nine = [c for c in code if len(
        [l for l in c if l in nineminusg]) == 5 and len(c) == 6]
    order[9] = nine[0]
    order[0] = [c for c in code if len(c) == 6 and len(
        [l for l in c if l in order[1]]) == 2 and c not in order][0]
    order[3] = [c for c in code if len(c) == 5 and len(
        [l for l in c if l in order[1]]) == 2 and c not in order][0]
    order[6] = [c for c in code if len(c) == 6 and c not in order][0]
    order[2] = [c for c in code if len(c) == 5 and len(
        [l for l in c if l not in order[6]]) == 1 and c not in order][0]
    order[5] = [c for c in code if c not in order][0]

    return [sorted(o) for o in order]


total = 0
for l in lines:
    line = ""

    order = (decodeLine(l))

    for n in l.split("|")[1].strip().split(" "):
        line += str(order.index(sorted(n)))

    print(line)
    total += int(line)

print(total)
