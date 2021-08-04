name = input("Please enter name of the patient: ")
age = int(input("Please enter age of the patient: "))

def new_patient(name, age):
    if name == "John Smith" and age == 20:
        print(True)
    else:
        print(False)

new_patient(name, age)