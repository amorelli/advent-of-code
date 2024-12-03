data = open('test.txt').readlines()

forest = [[int(x) for x in row.strip()] for row in data]
forest2 = list(zip(*forest))

s = 0
for i in range(len(forest[0])):
    for j in range(len(forest)):
        tree = forest[i][j]
        if all(x < tree for x in forest[i][0:j]) or \
                all(x < tree for x in forest[i][j+1:]) or \
                all(x < tree for x in forest2[j][0:i]) or \
                all(x < tree for x in forest2[j][i+1:]):
            s += 1

print(s)
