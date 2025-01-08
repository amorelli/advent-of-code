def simulate_guard_patrol(lab_map):
    grid = [list(row) for row in lab_map.splitlines()]
    rows, cols = len(grid), len(grid[0])

    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    direction_map = {'^': 1, '>': 2, 'v': 3, '<': 0}
    start_pos = None
    current_dir = None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in direction_map:
                start_pos = (r, c)
                current_dir = direction_map[grid[r][c]]
                grid[r][c] = '.'

    visited = set()
    current_pos = start_pos
    visited.add(current_pos)

    while True:
        dr, dc = directions[current_dir]
        next_pos = (current_pos[0] + dr, current_pos[1] + dc)

        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            break

        if grid[next_pos[0]][next_pos[1]] == '#':
            current_dir = (current_dir + 1) % 4
        else:
            current_pos = next_pos
            visited.add(current_pos)

    return len(visited)

def find_loop_positions(lab_map):
    grid = [list(row) for row in lab_map.splitlines()]
    rows, cols = len(grid), len(grid[0])

    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    direction_map = {'^': 1, '>': 2, 'v': 3, '<': 0}
    start_pos = None
    current_dir = None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in direction_map:
                start_pos = (r, c)
                current_dir = direction_map[grid[r][c]]
                grid[r][c] = '.'

    def causes_loop(obstruction_pos):
        temp_grid = [row[:] for row in grid]
        temp_grid[obstruction_pos[0]][obstruction_pos[1]] = '#'

        visited_with_dir = set()
        current_pos = start_pos
        current_dir_local = current_dir

        while True:
            dr, dc = directions[current_dir_local]
            next_pos = (current_pos[0] + dr, current_pos[1] + dc)

            if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
                return False
            
            if temp_grid[next_pos[0]][next_pos[1]] == '#':
                current_dir_local = (current_dir_local + 1) % 4
            else:
                current_pos = next_pos

            state = (current_pos, current_dir_local)
            if state in visited_with_dir:
                return True
            visited_with_dir.add(state)

    loop_positions = []
    for r in range(rows):
        for c in range(cols):
            if (r, c) != start_pos and grid[r][c] == '.':
                if causes_loop((r, c)):
                    loop_positions.append((r, c))

    return loop_positions

with open('input.txt', 'r') as file:
    lab_map = file.read()

distinct_positions = simulate_guard_patrol(lab_map)
print("Distinct positions visited:", distinct_positions)

loop_positions = find_loop_positions(lab_map)
print("Number of loop-causing positions:", len(loop_positions))
