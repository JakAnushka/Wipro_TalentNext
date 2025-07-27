'''Project:1 Write a Python function that accepts a hyphen-separated sequence of colors as input and returns the colors in a hyphen-separated sequence after sorting them alphabetically.

Constraint: All the colors will be completely in either lower case or upper case.

Sample input 1: green-red-yellow-black-white

Sample output 1: black-green-red-white-yellow

Sample input 2: PINK-BLUE-TAN-PURPLE

Sample output 2: BLUE-PINK-PURPLE-TAN'''
def sort_colors(color_sequence):
    colors = color_sequence.split('-')
    colors.sort()
    return '-'.join(colors)
user_input=input("Enter color sequence")
print(sort_colors(user_input))

'''Project:2 Create a Python module with the following functions:
Note: name will be completely in either lower case or upper case.

Import the module in another python script and test the functions by passing appropriate inputs.

Sample input 1: bob

Sample output 1:

Yes it is a palindrome.

No of vowels: 1

Frequency of letters: b-2, 0-1'''

def ispalindrome(name):
    if name == name[::-1]:
        print("Yes it is a palindrome.")
    else:
        print("No it is not a palindrome.")

def count_the_vowels(name):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in name if char in vowels)
    print(f"No of vowels: {count}")

def frequency_of_letters(name):
    freq = {}
    for char in name:
        freq[char] = freq.get(char, 0) + 1

    print("Frequency of letters:")
    for char in sorted(freq):
        print(f"{char}-{freq[char]}", end=", ")
    print()
