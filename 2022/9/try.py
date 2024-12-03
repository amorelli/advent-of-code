def calc(p1x, p1y, p2x, p2y):
    dist = abs(p1x - p2x) + abs(p1y - p2y)
    if p1x == p2x and dist >= 2:
        return (p2x, p1y - 1 if p1y > p2y else p1y + 1)
    if p1y == p2y and dist >= 2:
        return (p1x - 1 if p1x > p2x else p1x + 1, p2y)
    if dist > 2:
        if p1x > p2x:
            return (p2x + 1, p2y + 1 if p1y > p2y else p2y - 1)
        if p1x < p2x:
            return (p2x - 1, p2y + 1 if p1y > p2y else p2y - 1)
    return (p2x, p2y)


data = open("input.txt").read().strip()
moves = {"U": 1, "D": -1, "R": 1, "L": -1}
knots = {i: [(0, 0)] for i in range(10)}
for rd, line in enumerate(data.split("\n")):
    d, n = line.split()[0], int(line.split()[1])
    for i in range(n):
        hx, hy = knots[0][-1]
        hx += moves[d] if d in ["R", "L"] else 0
        hy += moves[d] if d in ["U", "D"] else 0
        knots[0].append((hx, hy))
        for k in range(1, 10):
            tx, ty = calc(*knots[k-1][-1], *knots[k][-1])
            knots[k].append((tx, ty))
print(f"Part 1: {len(set(knots[1]))}")
print(f"Part 2: {len(set(knots[9]))}")
