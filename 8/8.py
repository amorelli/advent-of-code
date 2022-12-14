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


def search(line_index, line, orientation):
    largest_item_in_list = max(line)
    indices_of_largest_item = find_indices(line, largest_item_in_list)
    # print("appending:", indices_of_largest_item[0], "and", indices_of_largest_item[-1])
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
    # print("line:", line_index, "searching left:", newline)
    if len(newline) > 0:
        largest_item = max(newline)
        # indices_of_largest_item = find_indices(newline, largest_item)
        index_of_largest = line.index(largest_item)
        if orientation == "horiz":
            print("appending from left:", line_index, index_of_largest)
            append_to_visible((line_index, index_of_largest))
        else:
            print("appending from left:", index_of_largest, line_index)
            append_to_visible((index_of_largest, line_index))
        search_left(line_index, line, index_of_largest, orientation)
        return index_of_largest


def search_right(line_index, line, bound, orientation):
    newline = line[bound + 1 : len(line)]
    # print("line:", line_index, "searching right:", newline)
    if len(newline) > 0:
        largest_item = max(newline)
        indices_of_largest = find_indices(line, largest_item)
        if orientation == "horiz":
            # print("appending from right:", line_index, indices_of_largest[-1])
            append_to_visible((line_index, indices_of_largest[-1]))
        else:
            # print("appending from right:", indices_of_largest[-1], line_index)
            append_to_visible((indices_of_largest[-1], line_index))
        if len(indices_of_largest) > 1:
            search_right(line_index, line, indices_of_largest[-1], orientation)
            return indices_of_largest[-1]


vertical_lists = {}

for ii, i in enumerate(forest):
    search(ii, i, "horiz")
    for ij, j in enumerate(i):
        edges = [0, len(i) - 1]
        if ii in edges or ij in edges:
            append_to_visible((ii, ij))
        if ij not in vertical_lists.keys():
            vertical_lists[ij] = [j]
        else:
            vertical_lists[ij].append(j)

for key, line in vertical_lists.items():
    search(key, line, "vert")


# visible_sort = sorted(visible, key=lambda element: (element[0], element[1]))
# print(visible_sort)
print("num visible", len(visible))
