'''Write a LC program to create an output dictionary
which contains only the odd numbers that are
present in the input list = [1,2,3,4,5,6,7] as
keys and their cubes as values.'''
input_list = [1, 2, 3, 4, 5, 6, 7]
output_dict = {x: x**3 for x in input_list if x % 2 != 0}
print(output_dict)


'''Make a dictionary of the 26 english alphabets mapping each with the corresponding integer

List'''
import string

alphabet_dict = {letter: index for index, letter in enumerate(string.ascii_lowercase, start=1)}
print(alphabet_dict)
