def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Start")
greet_user("John", "Smith")  # Positional Arguments
# greet_user("Mary")
print("Finish")
# greet_user(first_name="John", "Smith") # ERROR, Always Positional  Argument first then Key Word argument!
greet_user(last_name="Smith", first_name="John")  # Key Words Arguments
