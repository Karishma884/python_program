#Find all prime numbers  between 1 and 50 using nested for and if.
prime_numbers = []

for num in range(2, 51):  # Start from 2 since 1 is not a prime number
    is_prime = True  # Assume the number is prime

    for i in range(2, int(num**0.5) + 1):  # Check divisibility up to the square root of num
        if num % i == 0:  # If num is divisible by i, it's not prime
            is_prime = False
            break  # No need to check further

    if is_prime:
        prime_numbers.append(num)

print("Prime numbers between 1 and 50:", prime_numbers)
