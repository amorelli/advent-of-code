visible = []
forest = []

with open("input.txt", "r+") as file:
    for line in file:
        forest.append(list(map(int, line.strip())))


def find_indices(list, item_to_find):
    indices = []
    for idx, value in enumerate(list):
        if value == item_to_find:
            indices.append(idx)
    return indices


def append_to_visible(coord):
    if coord not in visible:
        visible.append(coord)


# Find instances of tallest tree in line.
# Then search left and right from those trees for tallest tree.
def search(line_index, line, orientation):
    largest_item_in_list = max(line)
    indices_of_largest_item = find_indices(line, largest_item_in_list)

    if orientation == "horiz":
        append_to_visible((line_index, indices_of_largest_item[0]))
        append_to_visible((line_index, indices_of_largest_item[-1]))
    else:
        append_to_visible((indices_of_largest_item[0], line_index))
        append_to_visible((indices_of_largest_item[-1], line_index))

    search_left(line_index, line, indices_of_largest_item[0], orientation)
    search_right(line_index, line, indices_of_largest_item[-1], orientation)


def search_left(line_index, line, bound, orientation):
    newline = line[0:bound]
    if len(newline) > 0:
        largest_item = max(newline)
        index_of_largest = line.index(largest_item)
        if orientation == "horiz":
            append_to_visible((line_index, index_of_largest))
        else:
            append_to_visible((index_of_largest, line_index))
        search_left(line_index, line, index_of_largest, orientation)
        return index_of_largest


def search_right(line_index, line, bound, orientation):
    newline = line[bound + 1 : len(line)]
    if len(newline) > 0:
        largest_item = max(newline)
        indices_of_largest = find_indices(line, largest_item)
        if orientation == "horiz":
            append_to_visible((line_index, indices_of_largest[-1]))
        else:
            append_to_visible((indices_of_largest[-1], line_index))
        if len(indices_of_largest) > 1:
            search_right(line_index, line, indices_of_largest[-1], orientation)
            return indices_of_largest[-1]


vertical_lists = {}
vision_scores = {}


def get_vision_score(val, search_array, orientation):
    vision_score = 0
    if orientation == "left":
        search_array.reverse()
    if isinstance(search_array, list) and len(search_array) > 0:
        for x in search_array:
            if x < val:
                vision_score += 1
            else:
                return vision_score + 1
        return vision_score
    else:
        return vision_score


def append_vision_scores(coords, score):
    if coords not in vision_scores.keys():
        vision_scores[coords] = [score]
    else:
        vision_scores[coords].append(score)


# Main loop
for ii, i in enumerate(forest):
    search(ii, i, "horiz")
    for ij, j in enumerate(i):
        # Get vision scores for part 2
        vs_right = get_vision_score(j, i[ij + 1 : len(i)], "right")
        append_vision_scores(str(ii) + "." + str(ij), vs_right)
        vs_left = get_vision_score(j, i[0:ij], "left")
        append_vision_scores(str(ii) + "." + str(ij), vs_left)
        # Check edges for part 1
        edges = [0, len(i) - 1]
        if ii in edges or ij in edges:
            append_to_visible((ii, ij))
        if ij not in vertical_lists.keys():
            vertical_lists[ij] = [j]
        else:
            vertical_lists[ij].append(j)

# Search vertically
for key, line in vertical_lists.items():
    search(key, line, "vert")
    # Get vision scores
    for il, l in enumerate(line):
        vs_down = get_vision_score(l, line[il + 1 : len(line)], "right")
        append_vision_scores(str(il) + "." + str(key), vs_down)
        vs_up = get_vision_score(l, line[0:il], "left")
        append_vision_scores(str(il) + "." + str(key), vs_up)

vision_scores_raw = []


def get_largest_vision():
    vscores = list(vision_scores.values())
    for scores in vscores:
        product = 1
        for s in scores:
            if s != 0:
                product *= s
        vision_scores_raw.append(product)
    return vision_scores_raw


print("num visible:", len(visible))
print("largest vision score:", max(get_largest_vision()))
