#Find the average of numbers in a list using a for loop.
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
total_sum = 0
count = 0

for num in numbers:
    total_sum += num
    count += 1

average = total_sum / count
print(average)
