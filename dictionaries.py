"""Name: John Smith
Email: john@gmail.com
Phone: 1234 """

customer = {
    "name": "John Smith",
    "age": 30,
    # "age": 40 # Duplication is not allowed
    "is_verified": True
}

customer["name"] = "Jack Smith" #Update the value!
print(customer["name"])

# print(customer["Name"]) dictionaries key sensitive!!!
# print(customer["birthdate"]) ERROR
print(customer.get("birthdate")) # returns none not an error!
print(customer.get("birthdate", "Jan 1 1980")) # supplying default value!

print(customer.get("age"))
customer["birthdate"] = "Sep 1  1980" # Adding new key
print(customer.get("birthdate"))

