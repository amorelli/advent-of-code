grid = []

with open('input.txt', 'r') as file:
    for line in file:
        row = list(line.strip())
        grid.append(row)

height = len(grid)
width = len(grid[0])
word = "XMAS"
visited = set()
found = 0
directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def dfs(row, col, wordIndex, direction):
    if wordIndex == len(word):
        return True
    if row < 0 or row >= height or col < 0 or col >= width:
        return False
    if (row, col) in visited:
        return False
    if grid[row][col] != word[wordIndex]:
        return False
        
    visited.add((row, col))
    result = dfs(row + direction[0], col + direction[1], wordIndex + 1, direction)
    visited.remove((row, col))
    return result

for i in range(height):
    for j in range(width):
        if grid[i][j] == word[0]:
            for direction in directions:
                if dfs(i, j, 0, direction):
                    found += 1
                    
print("found:", found)