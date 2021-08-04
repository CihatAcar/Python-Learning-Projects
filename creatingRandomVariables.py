import random

for i in range(3):
    print(random.random())  # Create random float numbers between 0 and 1
    print(random.randint(10, 20))  # Create random integer numbers in given ranges

members = ["Bengisu", "Evin", "Irem", "Cihat"]
leader = random.choice(members)
print(leader)
