head_moves = [[0, 0]]
tail_moves = [[0, 0]]

# plot head move to head_moves


def plot_pos(direction, move, current_pos):
    x = current_pos[1]
    y = current_pos[0]
    new_pos = [y, x]
    if direction == "U":
        new_pos[0] = y - move
    if direction == "D":
        new_pos[0] = y + move
    if direction == "R":
        new_pos[1] = x + move
    if direction == "L":
        new_pos[1] = x - move
    head_moves.append(new_pos)
    return new_pos


with open("test.txt") as input_file:
    for line in input_file:
        c = line.strip().split()
        plot_pos(c[0], int(c[1]), head_moves[-1])


print(head_moves)
