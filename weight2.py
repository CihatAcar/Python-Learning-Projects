weight = float(input("Please enter your weight either in kg or lbs: "))

kg_lbs = input("(K)g or (L)bs : ")

if kg_lbs.upper() == "K":
    converted_weight = weight / 0.
    print("You are %.2f lbs" % converted_weight)
    # print(f"You are {converted_weight} lbs")

elif kg_lbs.upper() == "L":
    converted_weight = weight * 0.45
    print("You are %.2f kg" % converted_weight)
    # print(f"You are {converted_weight} kg")
else:
    print("Please enter correct letter!")
