# from collections import defaultdict
from itertools import accumulate


# dirs = defaultdict(int)

# for line in open('input.txt'):
#     match line.split():
#         case '$', 'cd', '/': curr = ['/']
#         case '$', 'cd', '..': curr.pop()
#         case '$', 'cd', x: curr.append(x+'/')
#         case '$', 'ls': pass
#         case 'dir', _: pass
#         case size, _:
#             for p in accumulate(curr):
#                 dirs[p] += int(size)

# print(sum(s for s in dirs.values() if s <= 100_000),
#       min(s for s in dirs.values() if s >= dirs['/'] - 40_000_000))

dirs = {'/': 0}
cd = ['/']
with open("input.txt", "r") as f:
    for l in f.readlines():
        ls = l[:-1].split(" ")
        print(ls)
        if ls[0] == '$':
            if ls[1] == 'cd':
                if ls[2] == '..':
                    cd.pop()
                elif ls[2] == '/':
                    cd = ['/']
                else:
                    cd.append(ls[2])
        elif ls[0] == 'dir':
            dirs["".join(cd) + ls[1]] = 0
        else:
            dirs["".join(cd)] += int(ls[0])
            for i in range(1, len(cd)):
                dirs["".join(cd[:-i])] += int(ls[0])
print(sum(v for v in dirs.values() if v <= 100000))
print(min(v for v in dirs.values() if v >= dirs['/'] - 40000000))
