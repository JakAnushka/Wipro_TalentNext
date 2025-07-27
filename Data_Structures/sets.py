'''1. Write a program to remove a given item from the set.'''
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print("After removing 3:", my_set)

'''2. Write a program to create an intersection of sets.'''
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection = set1.intersection(set2)
print("Intersection:", intersection)

'''3.Write a program to create an union of sets.'''
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union:", union_set)

'''4.Write a program to find the maximum and minimum value in a set.'''
my_set = {10, 20, 5, 40, 25}
max_val = max(my_set)
min_val = min(my_set)
print("Maximum:", max_val)
print("Minimum:", min_val)
