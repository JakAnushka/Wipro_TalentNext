'''1.Write a program to accept two numbers as command line arguments and display their sum.'''

import sys

if len(sys.argv) != 3:
    print("Please provide exactly two numbers.")
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[2])

print("Sum:", a + b)

'''2.Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.'''

import sys

if len(sys.argv) != 2:
    print("Usage: python welcome.py <welcome_message>")
    sys.exit(1)

filename = sys.argv[0]         # This is the script name
message = sys.argv[1]          # This is the welcome message

print(f"{filename}: {message}")

'''3.Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them'''

import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if len(sys.argv) != 11:
    print("Please provide exactly 10 numbers.")
    sys.exit(1)

numbers = list(map(int, sys.argv[1:]))  # Skip script name

prime_sum = sum(num for num in numbers if is_prime(num))

print("Sum of prime numbers:", prime_sum)
