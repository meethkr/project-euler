sum_of_first_hundred_numbers = 100 * 101 / 2
square_of_sum_of_first_hundred_numbers = sum_of_first_hundred_numbers ** 2

squares_of_first_hundred_numbers = [x ** 2 for x in range(1, 101)]
sum_of_squares_of_first_hundred_numbers = sum(squares_of_first_hundred_numbers)

required_difference = square_of_sum_of_first_hundred_numbers - sum_of_squares_of_first_hundred_numbers
print(required_difference)