while guess_count < guess_limit:
    guess = int(input("Please guess the number!"))
    guess_count += 1
    if guess == number:
        print("You win!")
        break
else:
    print("Game over!")