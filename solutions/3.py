from math import sqrt

given_number = 600851475143

prime_factors = []

if given_number % 2 == 0:
    prime_factors.append(2)
    while given_number % 2 == 0:
        given_number = given_number / 2

i = 3
max_factor_possible = sqrt(given_number)
while i <= max_factor_possible:
    if given_number % i == 0:
        prime_factors.append(i)
        while given_number % i == 0:
            given_number = given_number / i

    i = i + 2

print(prime_factors)
print(max(prime_factors))

