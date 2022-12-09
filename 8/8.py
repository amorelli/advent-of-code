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


# Main search loop - Run search functions based on distance, break if func returns true
#   for keys in closest():
#     if search_funcs[key]():
#       append (ii, ij) to visible
#       break

# bool check_right: increment j, if node is larger, continue
# bool check_left: decrement j, if node is larger, continue
# bool check_up: decrement i, if node is larger, continue
# bool check_down: increment i, if node is larger, continue


def direction(x, op):
    return op(x)


def search(val, origin_index, cur_index, forest, direction_func, dir):
    print(
        "searching",
        val,
        "at",
        origin_index,
        "current index",
        cur_index,
        "direction",
        dir,
    )
    next_index = direction(cur_index, direction_func)
    # if vert: increment/decrement first i, second is static
    # if horiz: first i is static, increment/decrement second index
    if forest[origin_index if dir == "horiz" else next_index][
        origin_index if dir == "vert" else next_index
    ]:
        if (
            forest[origin_index if dir == "horiz" else next_index][
                origin_index if dir == "vert" else next_index
            ]
            < val
        ):
            search(val, origin_index, next_index, forest, direction_func, dir)
        else:
            return False
    else:
        return True


# strict horizontal search
# def search_horiz(val, cur_index, next_index, line, direction):
#   next_index = direction(cur_index)
#   if line[next_index]:
#     if line[next_index] < val:
#       search_horiz(val, next_index, direction(next_index), line, direction)
#     else:
#       return False
#   else:
#     return True

# map search functions to labels
search_lambdas = {
    "up": (lambda a: a + 1),
    "left": (lambda a: a - 1),
    "down": (lambda a: a + 1),
    "right": (lambda a: a + 1),
}

forest = []
# build forest
with open("input.txt", "r+") as file:
    length = 0
    height = 0
    for line in file:
        height += 1
        length = get_length(line)
        forest.append(list(map(int, line.strip())))

print(forest)

for ii, i in enumerate(forest):
    print(ii, i)
    for ij, j in enumerate(i):
        print("location: ", ii, ",", ij, "height: ", j)
        edists = edge_distances(ii, ij)
        print(edists)
        for key in edists.keys():
            if search(j, ij, ij, forest, search_lambdas[key], key):
                visible.append((ii, ij))
                break
    print(length, height)

# check up, down, left right in a line
# if no neighbours, node is edge

print(visible)
