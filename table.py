table = []

for x in range(1,11):
    minitable = []
    for y in range(0,11):
        minitable.append(x*y)
    table.append(minitable)

print(table)
