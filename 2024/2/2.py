# Initialize empty array and safe counter
numbers = []
safe_count = 0

# Read the file and process each line
with open('input.txt', 'r') as file:
    for line in file:
        # Split each line into numbers and convert to integers
        row = list(map(int, line.strip().split()))
        numbers.append(row)

# Check each row for safety
for row in numbers:
    is_safe = True
    increasing = None
    free_pass = True
    
    # Check differences between adjacent numbers
    for i in range(len(row) - 1):
        diff = row[i + 1] - row[i]
        
        if diff == 0:
            if free_pass:
                free_pass = False
                continue
            else:
                is_safe = False
                break
        
        # First difference determines if we're checking for increasing or decreasing
        if increasing is None:
            increasing = diff > 0
        
        # Check if difference is within ±3 and maintains same direction
        if abs(diff) > 3 or (diff > 0) != increasing:
            if free_pass:
                free_pass = False
                continue
            else:
                is_safe = False
                break
    
    if is_safe:
        safe_count += 1

print(safe_count)