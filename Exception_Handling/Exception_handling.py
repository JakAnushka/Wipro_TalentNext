'''Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result.'''
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a / b
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")
else:
    print("Result of division:", result)


'''Write a program to accept a number from the user and check whether it's prime or not. If user enters anything other than number, handle the exception and print an error message.'''
try:
    num = int(input("Enter a number: "))
    if num <= 1:
        print("Not a prime number.")
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print("Not a prime number.")
                break
        else:
            print("It is a prime number.")
except ValueError:
    print("Error: Please enter a valid integer.")


'''Write a program to accept the file name to be opened from the user, if file exist print the contents of the file in title case or else handle the exception and print an error message.'''
filename = input("Enter the filename to open: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile Content in Title Case:\n")
        print(content.title())
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An error occurred:", e)


'''Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. 
If any invalid index is entered, handle the exception and print an error message.'''
numbers = [10, -4, 23, -9, 18, -2, 0, 45, -11, 5]

try:
    index = int(input("Enter an index (0-9): "))
    number = numbers[index]
    if number > 0:
        print(f"Number at index {index} is positive.")
    elif number < 0:
        print(f"Number at index {index} is negative.")
    else:
        print(f"Number at index {index} is zero.")
except IndexError:
    print("Error: Index out of range. Valid range is 0 to 9.")
except ValueError:
    print("Error: Please enter a valid integer index.")
