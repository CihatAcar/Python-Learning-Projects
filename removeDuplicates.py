numbers = [1, 2, 3, 4, 1, 1, 5, 5, 18, 2, 3, 5]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)
