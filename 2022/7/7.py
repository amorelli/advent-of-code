directories = {'/': 0}
path = ['/']

with open("input.txt") as input_file:
    for line in input_file:
        lc = line.strip().split()
        if lc[0] == "$":
            arg1 = lc[1]
            if arg1 == 'cd':
                directory = lc[2]
                if directory == '..':
                    path.pop()
                elif directory == '/':
                    path = ['/']
                else:
                    path.append(directory)
        elif lc[0] == "dir":
            directory = lc[1]
            directories.setdefault("".join(path) + directory, 0)

        elif lc[0].isdigit():
            file_size = int(lc[0])
            file_path = "".join(path)
            directories[file_path] += file_size
            for i in range(1, len(path)):
                directories["".join(path[:-i])] += file_size

under100k = 0
for key, value in directories.items():
    if value <= 100000:
        under100k += value

print('under 100k: ', under100k)

deletion = []
for value in directories.values():
    if value >= directories['/'] - 40000000:
        deletion.append(value)

print('Smallest dir to delete for update: ', min(deletion))
