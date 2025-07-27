'''Your friend has sent you a text file containing n lines. He sent a secret message with it, which tells you the place and time where you have to go and meet him.

He challenges you to find it out without seeing the content of the file. He has given hints to find it. Let's surprise him by breaking the challenge with our python code

Hints to find the secret message:

1. The number of lines in the file tells you the meeting time.

Note: 1 number of lines < 24

if the number of lines is exceeding 12, you need to convert it to 12 hour

format. For example,

If the number of lines is 15, then the meeting time is 3 PM.

If the number of lines is 10, then the meeting time is 10 AM.

2. The word appearing for the maximum number of times tells you the meeting place.

Note: Meeting place will be a street name.

For example,

If the word Oxford appears for the maximum number of times,

then meeting place is Oxford Street.

If the word Park appears for the maximum number of times, then meeting place is Park Street.
'''
from collections import Counter

with open("secret.txt", "r") as file:
    lines = file.readlines()

line_count = len(lines)

if line_count <= 12:
    meeting_time = f"{line_count} AM"
else:
    hour = line_count % 12
    if hour == 0:
        hour = 12
    meeting_time = f"{hour} PM"

words = []

for line in lines:

    line_words = line.strip().split()
    for word in line_words:
        clean_word = ''.join(filter(str.isalpha, word))
        if clean_word:
            words.append(clean_word.lower())

word_counts = Counter(words)
most_common_word, _ = word_counts.most_common(1)[0]
meeting_place = most_common_word.capitalize() + " Street"
print("Secret Meeting Details:")
print("Time:", meeting_time)
print("Place:", meeting_place)
