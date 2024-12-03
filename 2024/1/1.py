import time

# Record start time
start_time = time.time()

# Initialize empty lists
list1 = []
list2 = []

# Read the file and process each line
with open('input.txt', 'r') as file:
    for line in file:
        # Split each line into two numbers and convert to integers
        num1, num2 = map(int, line.strip().split())
        list1.append(num1)
        list2.append(num2)

# Sort both lists
list1.sort()
list2.sort()

# Calculate multiplication sum based on occurrences
multiplication_sum = 0
for num in list1:
    occurrences = list2.count(num)
    multiplication_sum += num * occurrences

print("\nMultiplication sum based on occurrences:", multiplication_sum)

# Calculate sum of absolute differences
total_difference = sum(abs(a - b) for a, b in zip(list1, list2))
print("Sum of absolute differences:", total_difference)

# Calculate and print execution time
execution_time = time.time() - start_time
print(f"\nExecution time: {execution_time:.4f} seconds")