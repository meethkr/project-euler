def is_palindrome(number):
    string_number = str(number)
    reverse_string_number = string_number[::-1]
    return True if string_number == reverse_string_number else False

curr_result = 0

for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        if is_palindrome(i * j):
            curr_result = max(curr_result, i * j)

print(curr_result)
