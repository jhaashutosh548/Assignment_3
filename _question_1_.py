def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Sample list
numbers = (8, 2, 3, 0, 7)

# Call the function to sum the numbers
result = sum_numbers(numbers)

# Print the result
print("Sum:", result)