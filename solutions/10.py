from math import sqrt

TWO_MILLION = 2000000

def sieve():
    is_prime = [True] * (TWO_MILLION + 1)
    is_prime[0] = False
    is_prime[1] = False
    
    for i in range(2, int(sqrt(TWO_MILLION + 1))):
        if not is_prime[i]:
            continue

        for j in range(i * i, TWO_MILLION + 1, i):
            is_prime[j] = False
    
    return is_prime

if __name__ == "__main__":
    is_prime = sieve()
    sum = 0
    for i in range(len(is_prime)):
        if is_prime[i]:
            sum = sum + i
        
    print(sum)