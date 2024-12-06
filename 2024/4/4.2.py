grid = []

with open('input.txt', 'r') as file:
    for line in file:
        row = list(line.strip())
        grid.append(row)

height = len(grid)
width = len(grid[0])
letters = ["M", "S"]
found = 0
directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
matches = {}

# Check all 4 directions, check if those indexes are in range, and if the value is either S or M
# save the directions as keys, and the letters as values. Check that opposite directions letters are not the same.
# Add one to found, reset the matches map

def search(row, col, direction):
    if row < 0 or row >= height or col < 0 or col >= width:
        return False

    if grid[row][col] in letters:
        matches[direction] = grid[row][col]
        return True
    
    return False

for i in range(height):
    for j in range(width):
        if grid[i][j] == "A":
            for direction in directions:
                search(i + direction[0], j + direction[1], direction)
            if len(matches) == 4:
                if matches[(1, 1)] != matches[(-1, -1)] and matches[(1, -1)] != matches[(-1, 1)]:
                    found = found + 1
            matches = {}
                    
print("found:", found)