fhand = open("./arrays/easy/pytext.txt")
counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(f"{fhand}\n ------")
print(f"{counts}\n ------")
print(type(counts))

counts = list(counts.items())
# convert dictionary to list to sort
print(type(counts))

for mx in range(len(counts) - 1, -1, -1):
    swapped = False
    for i in range(mx):
        if counts[i][1] < counts[i + 1][1]:
            counts[i], counts[i + 1] = counts[i + 1], counts[i]
            swapped = True
    if not swapped:
        break

for count in counts:
    print(count)
