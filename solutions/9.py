def find_triplet():
    for a in range(999, 1, -1):
        for b in range(a - 1, 1, -1):  
            c = 1000 - a - b
            if a * a + b * b == c * c:
                return a * b * c

print(find_triplet())
