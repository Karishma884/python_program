#Print numbers in a list untill a negative number is encountered using a while loop:
numbers = [1, 2, 3, 4, -1, 5, 6, -2, 7]
index = 0

while index < len(numbers):
    if numbers[index] < 0:
        break  # Exit the loop if a negative number is found
    print(numbers[index])
    index += 1
