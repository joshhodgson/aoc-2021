values = [f.strip("\n") for f in open("example.txt")]

h = sum(int(x.split(" ")[1]) for x in values if x.startswith("forward"))
d = sum(int(x.replace("up ", "down -").split(" ")
        [1]) for x in values if not x.startswith("forward"))
print(h*d)
