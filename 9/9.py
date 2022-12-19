head_moves = [[0, 0]]
tail_moves = [[0, 0]]

head_moves_tuples = [(0, 0)]

# plot head move to head_moves


def plot_pos(direction, move, current_pos):
    x = current_pos[1]
    y = current_pos[0]
    new_pos = [y, x]
    # new_pos_tuple = (y, x)
    for i in range(move):
        if direction == "U":
            new_pos[0] = new_pos[0] - 1
            # new_pos_tuple[0] = new_pos_tuple[0] - 1
        if direction == "D":
            new_pos[0] = new_pos[0] + 1
            # new_pos_tuple[0] = new_pos_tuple[0] + 1
        if direction == "R":
            new_pos[1] = new_pos[1] + 1
            # new_pos_tuple[1] = new_pos_tuple[1] + 1
        if direction == "L":
            new_pos[1] = new_pos[1] - 1
            # new_pos_tuple[1] = new_pos_tuple[1] - 1
    head_moves.append(new_pos)
    head_moves_tuples.append(tuple(new_pos))
    return new_pos


def draw_grid():
    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0
    for coord in head_moves:
        x = coord[0]
        y = coord[1]
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
    grid = []
    for y in range(max_y, min_y-1, -1):
        row = []
        for x in range(min_x, max_x+1):
            # print(y, x)
            if (x, y) in head_moves_tuples:
                # row.append("H" + str(x) + "," + str(y))
                row.append("H")
            else:
                row.append(".")
        grid.append(row)
        print("".join(row))
    print("max:", max_x, max_y, "min:", min_x, min_y)


with open("test.txt") as input_file:
    for line in input_file:
        c = line.strip().split()
        plot_pos(c[0], int(c[1]), head_moves[-1])


draw_grid()
print(head_moves_tuples)
# print(len(head_moves))
