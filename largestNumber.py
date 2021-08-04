# numbers = [39, 42, 51, 3, 5, 81, 72, 91]
def largest_number(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


