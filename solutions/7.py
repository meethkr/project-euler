primes = [2]

i = 3

while len(primes) < 10001:
    is_prime = True
    for prime in primes:
        if i % prime == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(i)

    i = i + 1


print(primes[10000])
