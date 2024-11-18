#print a pattern of stars using nasted for loops.
rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()  # Move to the next line after each row
