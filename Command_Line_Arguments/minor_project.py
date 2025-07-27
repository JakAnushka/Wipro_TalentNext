'''Through command line arguments three strings separated by space are given to you. Each string is a series of numbers separated by hyphen(-). You like all the numbers in string 1 and dislike all the numbers in string 2.

Third string contains the numbers given to you. Your initial happiness is 0.

When you encounter a number which is present in string 1, add 1 to your happiness, if it is present in string 2, add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Sample input 1:
3-1
5-7 1-5-3-8

Sample output 1: 1

Explanation:

Numbers in string 1:

3, 1

Numbers in string 2: 5, 7

Numbers given to you: 1, 5, 3,8

You gain 1 unit of happiness for numbers 1 and 3 which are in string 1. Your total happiness is 2 now.

You lose 1 unit of happiness for number 5 which is in string 2. Your total happiness in 1 now.

8 is not present in either of the strings, so your happiness does not change.

Final happiness is 1.'''

import sys

if len(sys.argv) != 4:
    print("Please provide exactly 3 arguments.")
    sys.exit(1)

like_str = sys.argv[1]
dislike_str = sys.argv[2]
numbers_str = sys.argv[3]

likes = set(map(int, like_str.split('-')))
dislikes = set(map(int, dislike_str.split('-')))
numbers = list(map(int, numbers_str.split('-')))

happiness = 0

for num in numbers:
    if num in likes:
        happiness += 1
    elif num in dislikes:
        happiness -= 1

print(happiness)
