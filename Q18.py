#python program to check if a given number is an Armstrong number.
def is_armstrong_number(num):
    digits = str(num)
    power = len(digits)
    sum_of_powers = sum(int(digit) ** power for digit in digits)
    return sum_of_powers == num
number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
