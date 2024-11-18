#Print the fibonacci sequence up to the 10th term.
n_terms = 10
fibonacci_sequence = []

# First two Fibonacci numbers
a, b = 0, 1

for _ in range(n_terms):
    fibonacci_sequence.append(a)
    a, b = b, a + b  # Update a and b

print("Fibonacci sequence up to the 10th term:", fibonacci_sequence)
