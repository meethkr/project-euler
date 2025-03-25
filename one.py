multiples_of_three_or_five = [x for x in range(1000) if (x % 3 == 0 or x % 5 == 0)]
# print(multiples_of_three_or_five)
print(sum(multiples_of_three_or_five))