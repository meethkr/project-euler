import math

primes = [2, 3, 5, 7, 11, 13, 17, 19]
powers = [0] * len(primes)

for i in range(2, 21):
    for j in range(len(primes)):
        power = 0
        while i % primes[j] == 0:
            power += 1
            i = i / primes[j]

        powers[j] = max(powers[j], power)


result = math.prod([primes[i] ** powers[i] for i in range(len(primes))])
print(result)
