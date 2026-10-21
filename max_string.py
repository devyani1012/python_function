def max_value(*strings):
    if len(strings) == 0:
        return None
    max_str = strings[0]
    for s in strings:
        if s > max_str:
            max_str = s
    return max_str

print(max_value('apple', 'Banana', 'cherry'))