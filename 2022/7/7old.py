directories = {}
path = ["/"]

with open("input.txt") as input_file:
    for line in input_file:
        lc = line.strip().split()
      #   print(lc)

        # user input
      #   print('path array', path)
        if lc[0] == "$":
            arg1 = lc[1]
            if arg1 == 'cd':
                directory = lc[2]
                if directory != '..':
                    path.append(directory)
                    directories.setdefault(path[0] + "/".join(path[1:]), 0)
                else:
                    path.pop()
      # these are files, not directories. Their size should be added to their parent directory.
        if lc[0] == "dir":
            directory = lc[1]
            if (len(path) > 1):
                directories.setdefault(
                    path[0] + "/".join(path[1:]) + "/" + directory, 0)
            else:
                directories.setdefault(
                    path[0] + directory, 0)

        if lc[0].isdigit():
            # print(path)
            file_size = int(lc[0])
            file_path = path[0] + "/".join(path[1:])
            # print('file_path', file_path, "alt", alt)
            if (len(path) > 1):
                directories[file_path] += file_size
            else:
                directories["/"] += file_size

roots = {}
for key, value in directories.items():
    root = "/" + key.split("/")[1]
    roots.setdefault(root, 0)
#     print(key, value)

under100k = 0
# for root in roots:
#     print(root)
#     if root != "/":
#         for key, value in directories.items():
#             print(key, value)
#             if key.startswith(root):
#                 #     print(key, root)
#                 for v in value:
#                     roots[root] += v
#                     if v <= 100000:
#                         under100k += v

for key, value in directories.items():
    print(key, value)
    if value <= 100000:
        under100k += value

# print(roots)
# print(under100k)
print(sum(v for v in directories.values() if v <= 100000))
# r = 0
# fsizes = {}
# for folder in directories:
#     fsize = 0
#     for file in files:
#         if file.startswith(folder):
#             fsize += files[file]
#     if fsize <= 100000:
#         r += fsize
#     fsizes[folder] = fsize

# print(r)

# print(directories)
