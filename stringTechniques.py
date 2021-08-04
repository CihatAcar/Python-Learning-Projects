course = "Python for Beginners"
print(course.upper())
print(course.lower())
print(course)
print(course.find("P")) #Gives the index of value if it exists
print(course.find("e")) #Its only gives the first index that the value exist
print(course.find("Beginners"))
print(course.find("O"))
print(course.replace("Beginners", "Absolute Beginners"))
print(course)

print(len(course))
print("Python" in course) # Check is it there or not and gives boolean value True or False
print("python" in course)