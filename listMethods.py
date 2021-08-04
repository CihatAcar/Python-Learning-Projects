numbers = [2, 3, 5, 1, 5, 3, 2, 7, 8]
numbers.append(20)
numbers.insert(0, 10)
numbers.remove(2)
# numbers.clear()
numbers.pop()
print(numbers.index(3))
print(50 in numbers)
print(numbers.count(3))
numbers.sort()
numbers.reverse()
numbers2 = numbers.copy()
numbers.append(15)
print(numbers)
print(numbers2)

s = """abacabaa"""