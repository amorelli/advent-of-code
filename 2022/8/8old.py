import functools

visible = []

# memoize


@functools.cache
def get_length(x):
    return len(x) - 1


# find closest edge before running search direction functions


def edge_distances(icoord, jcoord):
    dists = {}
    dists["up"] = icoord / height
    dists["left"] = jcoord / length
    dists["down"] = 1 - dists["up"]
    dists["right"] = 1 - dists["left"]
    return dict(sorted(dists.items(), key=lambda dists: dists[1]))


# bool check_right: increment j, if node is larger, continue
# bool check_left: decrement j, if node is larger, continue
# bool check_up: decrement i, if node is larger, continue
# bool check_down: increment i, if node is larger, continue


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

# strict horizontal search


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


# def search_up(val, coords, forest):
#     print("searching up for", val, "at", "%d,%d" % (coords[0], coords[1]))
#     next_coord = (coords[0] - 1, coords[1])
#     if next_coord[0] > 0:
#         print('cur val:', forest[next_coord[0]]
#               [next_coord[1]], "orig val:", val)
#         if forest[next_coord[0]][next_coord[1]] > val:
#             return False
#         else:
#             search_up(val, next_coord, forest)
#     else:
#         print("found edge searching up")
#         return True


# def search_down(val, coords, forest):
#     print("searching down for", val, "at", "%d,%d" % (coords[0], coords[1]))
#     next_coord = (coords[0] + 1, coords[1])
#     if next_coord[0] < 99:
#         print('cur val:', forest[next_coord[0]]
#               [next_coord[1]], "orig val:", val)
#         if forest[next_coord[0]][next_coord[1]] > val:
#             return False
#         else:
#             search_down(val, next_coord, forest)
#     else:
#         print("found edge searching down")
#         return True


def direction(x, op):
    return op(x)


def search(val, coords, forest, direction_func, dirct):
    print(
        "searching:",
        val,
        "coords:",
        coords,
        "dirct:",
        dirct,
    )
    horiz = ["left", "right"]
    # vert = ["up", "down"]
    # if vert: increment/decrement first i, second is static
    # if horiz: first i is static, increment/decrement second index

    vision_score = 0
    new_coords = (
        (coords[0], direction(coords[1], direction_func))
        if dirct in horiz
        else (direction(coords[0], direction_func), coords[1])
    )
    i1 = new_coords[0]
    i2 = new_coords[1]
    next_val = forest[i1][i2]

    while val > next_val:
        vision_score += 1
        new_coords = (
            (new_coords[0], direction(new_coords[1], direction_func))
            if dirct in horiz
            else (direction(new_coords[0], direction_func), new_coords[1])
        )
        i1 = new_coords[0]
        i2 = new_coords[1]
        print(i1, i2)
        print(vision_score)
        if 0 <= i1 < 99 and 0 <= i2 < 99:
            next_val = forest[i1][i2]
        else:
            break
    return vision_score
    # if 0 < i1 < 9 and 0 < i2 < 9:
    #     print("new_coords:", i1, i2)
    #     print(
    #         "forest[%d][%d]:" % (i1, i2),
    #         forest[i1][i2],
    #         "<",
    #         val,
    #         "?:",
    #         forest[i1][i2] < val,
    #     )
    #     if forest[i1][i2] < val:
    #         vision_score += 1
    #         search(val, new_coords, forest, direction_func, dirct)
    #     else:
    #         return vision_score
    # else:
    #     return vision_score


# map search functions to labels
search_lambdas = {
    "up": (lambda a: a + 1),
    "left": (lambda a: a - 1),
    "down": (lambda a: a + 1),
    "right": (lambda a: a + 1),
}

forest = []
# build forest
with open("test.txt", "r+") as file:
    length = 0
    height = 0
    for line in file:
        height += 1
        length = get_length(line)
        forest.append(list(map(int, line.strip())))

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

trees_vision = {}

for ii, i in enumerate(forest):
    # print(ii, i)
    for ij, j in enumerate(i):
        # print("ii, ij: ", ii, ",", ij, "val: ", j)
        edists = edge_distances(ii, ij)
        # print(edists)
        # edges = [0, 98]
        # if (ii in edges or ij in edges):
        #     visible.append((ii, ij))
        # else:
        for key in edists.keys():
            print(
                "search found?", search(j, (ij, ij), forest, search_lambdas[key], key)
            )
            score = search(j, (ij, ij), forest, search_lambdas[key], key)
            if ii + ij in trees_vision.keys():
                trees_vision[ii + ij].append(score)
            else:
                trees_vision[ii + ij] = [score]

print(trees_vision)

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
print("number of visible: ", len(visible) - 4)
