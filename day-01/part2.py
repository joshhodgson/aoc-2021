values = [int(f.strip("\n")) for f in open("input.txt")]
ranges=[]
for i in range(2,len(values)):
    ranges.append(values[i]+values[i-1]+values[i-2])
total=0
for i in range(1,len(ranges)):
    if ranges[i]>ranges[i-1]:
        total+=1
print(total)