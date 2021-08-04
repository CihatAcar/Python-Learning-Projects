# i = 1
#
# while i <= 10:
#     print("*" * i)
#     i += 1
# print("Done!")

number = 9
guess_count = 0
guess_limit = 3


while guess_count < guess_limit:
    guess = int(input("Please guess the number!"))
    guess_count += 1
    if guess == number:
        print("You win!")
        break
else:
    print("Game over!")
