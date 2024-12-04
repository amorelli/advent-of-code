import re

with open('input.txt', 'r') as file:
    content = file.read()
    
    # Split content into tokens that are either mul(x,y), do(), or don't()
    pattern = r'(?:mul\(\d+,\d+\)|do\(\)|don\'t\(\))'
    tokens = re.findall(pattern, content)
    
    total = 0
    include_numbers = True  # Flag to track whether to include multiplications
    
    for token in tokens:
        if token == "don't()":
            include_numbers = False
        elif token == "do()":
            include_numbers = True
        elif include_numbers:
            # Extract and multiply numbers if we're including them
            numbers = re.findall(r'mul\((\d+),(\d+)\)', token)
            if numbers:  # Will have 0 or 1 matches
                x, y = map(int, numbers[0])
                total += x * y
    
    print(f"Total: {total}")
