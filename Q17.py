#print number from 1 to 10. if a number is even, skip it using a for loop and else clause.
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    else:
        print(i)
