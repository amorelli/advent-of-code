# bool check_right: increment j, if node is larger, continue
# bool check_left: decrement j, if node is larger, continue
# bool check_up: decrement i, if node is larger, continue
# bool check_down: increment i, if node is larger, continue
import functools
visible = []
forest = []

with open("input.txt", "r+") as file:
    for line in file:
        forest.append(list(map(int, line.strip())))

# print(forest)


def find_indices(list, item_to_find):
    indices = []
    for idx, value in enumerate(list):
        if value == item_to_find:
            indices.append(idx)
    return indices


def append_to_visible(coord):
    # visible.append(coord)
    if coord not in visible:
        visible.append(coord)


def search_left(line_index, line, bound):
    newline = line[0:bound]
    print('line:', line_index, 'searching left:', newline)
    if len(newline) > 0:
        largest_item = max(newline)
        # indices_of_largest_item = find_indices(newline, largest_item)
        index_of_largest = line.index(largest_item)
        append_to_visible((line_index, index_of_largest))
        search_left(line_index, line, index_of_largest)
        return index_of_largest


def search_right(line_index, line, bound):
    newline = line[bound+1:len(line)]
    print('line:', line_index, 'searching right:', newline)
    if len(newline) > 0:
        largest_item = max(newline)
        # index_of_largest = line.reverse().index(largest_item)
        indices_of_largest = find_indices(line, largest_item)
        append_to_visible((line_index, indices_of_largest[-1]))
        if len(indices_of_largest) > 1:
            search_right(line_index, line, indices_of_largest[-1])
            return indices_of_largest[-1]

# def search_right(line_index, line):
#     print('line:', line_index, 'searching right:', line)
#     if len(line) > 0:
#         largest_item_in_list = max(line)
#         indices_of_largest_item = find_indices(line, largest_item_in_list)
#         remaining = line[indices_of_largest_item[-1]+1:len(line)]
#         if len(indices_of_largest_item) > 0:
#             append_to_visible((line_index, indices_of_largest_item[-1]))
#             search_right(line_index, remaining)
#             return indices_of_largest_item[-1]


# def search(line_index, line, left_bound, right_bound):


def search(line_index, line, istart, iend, dx):
    print('----------------------')
    print('dir:', dx)
    print("line index:", line_index)
    print('start:%d' % istart, 'end:%d' % iend)
    print('line to check: ', line[istart:iend])
    newline = line[istart:iend]
    if len(newline) > 0:
        largest_item_in_list = max(newline)
        # indices_of_largest_item = [index for index,
        #                            item in enumerate(line) if largest_item_in_list]

        indices_of_largest_item = find_indices(newline, largest_item_in_list)
        # print('line:', line)
        print('largest item:', largest_item_in_list)
        print('indices:', indices_of_largest_item)
        left_side = newline[0:indices_of_largest_item[0]]
        right_side = newline[indices_of_largest_item[-1]+1: len(newline)]
        print("l:", left_side, "r", right_side)

        if (len(indices_of_largest_item) > 1):
            if (dx == "right"):
                print('append from right:',
                      (line_index, indices_of_largest_item[-1]))
                append_to_visible((line_index, indices_of_largest_item[-1]))
                search(line_index, line,
                       indices_of_largest_item[-1]+1, len(line), "right")
            if (dx == "left"):
                print('append from left:',
                      (line_index, indices_of_largest_item[0]))
                append_to_visible((line_index, indices_of_largest_item[0]))
                search(line_index, line, 0, indices_of_largest_item[0], "left")
            if dx == "both":
                print('append both:', (line_index,
                      indices_of_largest_item[0]), (line_index, indices_of_largest_item[-1]))
                append_to_visible((line_index, indices_of_largest_item[0]))
                append_to_visible((line_index, indices_of_largest_item[-1]))
                search(line_index, line,
                       indices_of_largest_item[-1]+1, len(line), "right")
                search(line_index, line, 0, indices_of_largest_item[0], "left")
        else:
            print('append only i:', (line_index, indices_of_largest_item[0]))
            append_to_visible((line_index, indices_of_largest_item[0]))

    # for c in line:
    #     c = int(c)


vertical_lists = {}


for ii, i in enumerate(forest):
    # print(ii, i)
    # search(ii, i, 0, len(i), "both")
    print('-----------------')
    print('start search:', i)
    # left_side = i[:len(i)//2]
    # right_side = i[len(i)//2:]
    half = len(i)//2
    search_right(ii, i, half)
    search_left(ii, i, half)
    for ij, j in enumerate(i):
        edges = [0, len(i)-1]
        if (ii in edges or ij in edges):
            append_to_visible((ii, ij))

        if ij not in vertical_lists.keys():
            vertical_lists[ij] = [j]
        else:
            vertical_lists[ij].append(j)

    #     # print("ii, ij: ", ii, ",", ij, "val: ", j)
    #     edges = [0, 98]
    #     if (ii in edges or ij in edges):
    #         visible.append((ii, ij))
    #     else:
    #         search(i)


# search(0, [0, 3, 4, 2, 5, 4, 2, 1, 5, 3, 2, 4, 1], 0, -1)

for key, line in vertical_lists.items():
    # print(key, line)
    # left_side = i[:len(i)//2]
    # right_side = i[len(i)//2:]
    half = len(i)//2
    # search(key, line, 0, len(line), "both")
    search_right(ii, i, half)
    search_left(ii, i, half)


# print(vertical_lists)
# visible_sort = sorted(visible, key=lambda element: (element[0], element[1]))
# print(visible_sort)
print('num visible', len(visible))


# def search_right(val, cur_index, line):
#     print("searching right for", val, "at", "%d" % (cur_index), "in", line)
#     next_index = cur_index + 1
#     if next_index < 99:
#         print('cur val:', line[next_index], "orig val:", val)
#         if line[next_index] > val:
#             return False
#         else:
#             search_right(val, next_index, line)
#     else:
#         print("found edge searching right")
#         return True


# def search_left(val, cur_index, line):
#     print("searching left for", val, "at", "%d" % (cur_index), "in", line)
#     next_index = cur_index - 1
#     if next_index > 0:
#         print('cur val:', line[next_index], "orig val:", val)
#         if line[next_index] > val:
#             return False
#         else:
#             search_left(val, next_index, line)
#     else:
#         print("found edge searching left")
#         return True

# print("number of visible: ", len(visible)-4)

# def search(val, coords, forest, direction_func, dirct):
#     print(
#         "searching:",
#         val,
#         "coords:",
#         coords,
#         "dirct:",
#         dirct,
#     )
#     horiz = ["left", "right"]
#     # vert = ["up", "down"]
#     # if vert: increment/decrement first i, second is static
#     # if horiz: first i is static, increment/decrement second index

#     new_coords = (coords[0], direction(coords[1], direction_func)) if dirct in horiz else (
#         direction(coords[0], direction_func), coords[1])
#     i1 = new_coords[0]
#     i2 = new_coords[1]
#     if 0 < new_coords[0] < 99 and 0 < new_coords[1] < 99:
#         print("new_coords:", i1, i2)
#         print("forest[%d][%d]:" % (i1, i2), forest[i1][i2],
#               "<", val, "?:", forest[i1][i2] < val)
#         if forest[i1][i2] < val:
#             search(val, new_coords,
#                    forest, direction_func, dirct)
#         else:
#             return False
#     else:
#         return True

# def search(val, origin_index, cur_index, forest, direction_func, dirct):
#     print(
#         "searching:",
#         val,
#         "origin:",
#         origin_index,
#         "current index:",
#         cur_index,
#         "direction:",
#         dirct,
#     )
#     horiz = ["left", "right"]
#     vert = ["up", "down"]
#     next_index = direction(cur_index, direction_func)
#     print("next_index", next_index)
#     # if vert: increment/decrement first i, second is static
#     # if horiz: first i is static, increment/decrement second index
#     if 0 < next_index < 99:
#         i1 = origin_index if dirct in horiz else next_index
#         i2 = origin_index if dirct in vert else next_index
#         print("i1,i2:", i1, i2)
#         print("forest[%d][%d]:" % (i1, i2), forest[i1][i2],
#               "<", val, "?:", forest[i1][i2] < val)
#         if forest[i1][i2] < val:
#             search(val, origin_index, next_index,
#                    forest, direction_func, dirct)
#         else:
#             return False
#     else:
#         return True


# forest = []
# # build forest
# with open("input.txt", "r+") as file:
#     length = 0
#     height = 0
#     for line in file:
#         height += 1
#         length = get_length(line)
#         forest.append(list(map(int, line.strip())))

# print(forest)

# for ii, i in enumerate(forest):
#     # print(ii, i)
#     for ij, j in enumerate(i):
#         # print("ii, ij: ", ii, ",", ij, "val: ", j)
#         edists = edge_distances(ii, ij)
#         # print(edists)
#         edges = [0, 98]
#         if (ii in edges or ij in edges):
#             visible.append((ii, ij))
#         else:
#             for key in edists.keys():
#                 if key == "up":
#                     if search_up(j, (ii, ij), forest):
#                         visible.append((ii, ij))
#                         continue
#                 if key == "down":
#                     if search_down(j, (ii, ij), forest):
#                         visible.append((ii, ij))
#                         continue
#                 if key == "left":
#                     if search_left(j, ij, i):
#                         visible.append((ii, ij))
#                         continue
#                 if key == "right":
#                     if search_right(j, ij, i):
#                         visible.append((ii, ij))
#                         continue

# for ii, i in enumerate(forest):
#     # print(ii, i)
#     for ij, j in enumerate(i):
#         # print("ii, ij: ", ii, ",", ij, "val: ", j)
#         edists = edge_distances(ii, ij)
#         # print(edists)
#         edges = [0, 98]
#         if (ii in edges or ij in edges):
#             visible.append((ii, ij))
#         else:
#             for key in edists.keys():
#                 print("search found?", search(
#                     j, (ij, ij), forest, search_lambdas[key], key))
#                 if search(j, (ij, ij), forest, search_lambdas[key], key):
#                     visible.append((ii, ij))
#                     break

# for ii, i in enumerate(forest):
#     # print(ii, i)
#     for ij, j in enumerate(i):
#         # print("ii, ij: ", ii, ",", ij, "val: ", j)
#         edists = edge_distances(ii, ij)
#         # print(edists)
#         edges = [0, 98]
#         if (ii in edges or ij in edges):
#             visible.append((ii, ij))
#         else:
#             for key in edists.keys():
#                 print("search found?", search(
#                     j, ij, ij, forest, search_lambdas[key], key))
#                 if search(j, ij, ij, forest, search_lambdas[key], key):
#                     visible.append((ii, ij))
#                     break

# print(visible)
