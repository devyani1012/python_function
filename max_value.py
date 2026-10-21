def max_value(*numbers):
    if len(numbers) == 0:
        return None  # Return None if no numbers are provided
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
print(max_value(3, 5, 2, 8, 1))  # Output: 8
print(max_value('apple', 'Banana', 'cherry'))  # Output: cherry