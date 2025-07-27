'''1.Write a program to add a key and value to a dictionary.

Sample Dictionary: (0: 10, 1: 20)

Expected Result (0: 10, 1: 20, 2: 30)
'''
sample_dict = {0: 10, 1: 20}
sample_dict[2] = 30
print("Updated dictionary:", sample_dict)

'''2. Write a program to concatenate the following dictionaries to create a new one.

Sample Dictionary:

dicl=(1:10, 2:20) dic2=(3:30, 4:40) dic3=(5:50,6:60) Expected Result (1: 10, 2: 20, 3: 30, 4: 40, 5: 58, 6:60)
'''
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result = {**dic1, **dic2, **dic3}
print("Concatenated dictionary:", result)

'''3. Write a program to check if a given key already exists in a dictionary.'''
sample_dict = {1: 'apple', 2: 'banana', 3: 'cherry'}

key_to_check = 2

if key_to_check in sample_dict:
    print(f"Key {key_to_check} exists.")
else:
    print(f"Key {key_to_check} does not exist.")



''' 4. Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values.
'''
sample_dict = {'a': 1, 'b': 2, 'c': 3}

print("Keys:")
for key in sample_dict:
    print(key)

print("\nValues:")
for value in sample_dict.values():
    print(value)

print("\nKeys and Values:")
for key, value in sample_dict.items():
    print(f"{key}: {value}")

'''5.Write a program to prepare a dictionary where the keys are numbers between 1 and 15 (both included) 
and the values are square of the keys.'''
squares_dict = {x: x**2 for x in range(1, 16)}
print("Squares Dictionary:", squares_dict)


'''6. Write a program to sum all the values in a dictionary, considering the values will be of int type.'''
sample_dict = {'a': 10, 'b': 20, 'c': 30}
total = sum(sample_dict.values())
print("Sum of values:", total)
