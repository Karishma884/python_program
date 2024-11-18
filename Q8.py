#Count the number of the vowel in a string using a for loop.
my_string = "Hello, World!"
vowels = "aeiouAEIOU"
count = 0

for char in my_string:
    if char in vowels:
        count += 1

print(count)
