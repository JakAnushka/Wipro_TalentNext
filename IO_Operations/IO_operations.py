'''1. Write a program to read the entire content from a txt file and display it to the user.'''
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)


'''2. Write a program to read first n lines from a txt file. Get n as user input.'''
n = int(input("Enter number of lines to read: "))

with open("sample.txt", "r") as file:
    for i in range(n):
        line = file.readline()
        if not line:
            break
        print(line.strip())

'''3. Write a program to accept input from user and append it to a txt file.'''
text_to_append = input("Enter text to append to the file: ")

with open("sample.txt", "a") as file:
    file.write(text_to_append + "\n")

print("Text appended successfully.")

'''4. Write a program to read contents from a txt file line by line and store each line into a list.'''
with open("sample.txt", "r") as file:
    lines = file.readlines()

# Remove newline characters
line_list = [line.strip() for line in lines]
print("Lines stored in list:", line_list)

'''5. Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.'''
with open("sample.txt", "r") as file:
    content = file.read()
    words = content.split()

longest = max(words, key=len)
print("Longest word:", longest)

'''6. Write a program to count the frequency of a user entered word in a txt file.'''
search_word = input("Enter the word to count: ")

with open("sample.txt", "r") as file:
    content = file.read()
    words = content.split()

frequency = words.count(search_word)
print(f"Frequency of '{search_word}':", frequency)
