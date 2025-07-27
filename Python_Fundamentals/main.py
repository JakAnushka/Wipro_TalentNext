# Write a program to check if a given number is Positive, Negative or Zero.
def num_is_positive_negative_or_zero():
    num=int(input("Enter number:"))
    if num>0:
        print("Positive")
    elif num<0:
        print("Negative")
    else:
        print("Zero")


#Write a program to check if a given number is odd or even
def given_num_is_even_odd():
    num=int(input("Enter number:"))
    if num%2==0:
        print("given number is even")
    else:
        print("given number is odd")

#Given two non-negative values, print true if they have the same last digit, such as with 27 and 57
def last_digit_check():
    num1=int(input("Enter number 1:"))
    num2=int(input("Enter number 2:"))
    last_digit_of_1=num1%10
    last_digit_of_2=num2%10
    if (last_digit_of_1==last_digit_of_2):
        print("True")
    else:
        print("False")

#Write a program to print numbers from 1 to 10 in a single row with one tab space.
def print_num_1_to_100():
    for i in range(1,10):
        print(i,end=" ")

#Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.
def even_numbers_23_and_57():
    for i in range(23,57):
        if i%2==0:
            print(i)

#Write a program to check if a given number is prime or not.
def prime_or_not():
    num_given_number=int(input("enter number:"))
    cnt=0
    for i in range(1,num_given_number+1):
        if num_given_number%i==0:
            cnt+=1
    if cnt>2 or cnt<2:
        print("not prime")
    if cnt==2:
        print("prime")

# Write a program to print prime numbers between 10 and 99.
def prime_numbers_between_10_and_99():
    for i in range(10,99):
        cnt = 0
        for j in range(1, i + 1):
            if i%j==0:
                cnt+=1
        if cnt==2:
            print(i)

# Write a program to print the sum of all the digits of a given number.
def sum_of_all_digits():
    digit=int(input("enter a number"))
    sum=0
    while digit>0:
        r=digit%10
        sum+=r
        digit/=10
    print(sum)

# Write a program to reverse a given number and print
def reverse_num():
    digit=int(input("enter a number"))
    rev=0
    while digit>0:
        r=digit%10
        rev=rev*10+r
        digit//=10
    print(rev)


# Write a program to find if the given number is palindrom or not.
def num_is_palindrom():
    digit=int(input("enter a number"))
    org_num=digit
    rev=0
    while digit>0:
        r=digit%10
        rev=rev*10+r
        digit//=10
    if rev==org_num:
        print("Palindrome")
    else:
        print("Not Palindrome")
