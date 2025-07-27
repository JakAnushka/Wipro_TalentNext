'''1.Write a program to count the number of upper and lower case letters in a String.'''
text = "Hello World!"
upper_count = 0
lower_count = 0

for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)


'''2.Write a program that will check whether a given String is Palindrome or not.'''
s = "madam"
if s == s[::-1]:
    print(f'"{s}" is a palindrome.')
else:
    print(f'"{s}" is not a palindrome.')


'''3.Given a string, return a new string made of n copies of the first 2 chars of the original string where n is the length of

the string. The string length will be >=2. If input is "Wipro" then output should be "Wiwiwiwiwi".'''
s = "Wipro"
first_two = s[:2]
result = first_two * len(s)
print("Result:", result)

'''4.Given a string, if the first or last character is 'x', return the string without those 'x' character, else return the string unchanged. If the input is "xHix", then output is "Hi".'''
s = "xHix"
if s.startswith('x'):
    s = s[1:]
if s.endswith('x'):
    s = s[:-1]
print("Modified string:", s)

'''5.Given a string and an integer n, return a string made of n repetitions of the last n characters of the string. You may assume that n is between 0 and the length of the string inclusive.
 For example if the inputs are "Wipro" and 3, then the output should be "propropro".'''
s = "Wipro"
n = 3
last_n = s[-n:]
result = last_n * n
print("Result:", result)
