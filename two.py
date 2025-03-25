FOUR_MILLION=4000000

def fib(limit):
    x = [0, 1, 1]
    i = 1

    while i < limit:
        i = x[-1]
        j = x[-2]
        x.append(i + j)

    return x



fibonacci_sequence = fib(FOUR_MILLION)
# print(fibonacci_sequence)
even_fibonacci_numbers = [x for x in fibonacci_sequence if x % 2 == 0]
required_sum = sum(even_fibonacci_numbers)

print(required_sum)