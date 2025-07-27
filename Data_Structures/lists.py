'''.Write a program to create a list of 5 integers and display the list items.
Access individual elements through index.'''

numbers = [10, 20, 30, 40, 50]

print("List:", numbers)

print("First element:", numbers[0])
print("Second element:", numbers[1])
print("Third element:", numbers[2])
print("Fourth element:", numbers[3])
print("Fifth element:", numbers[4])

'''2.Write a program to append a new item to the end of the list'''
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print("After append:", numbers)

'''3.Write a program to reverse the order of the items in the list.'''
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print("Reversed list:", numbers)

'''4.Write a program to print the number of occurrences of a specified element in a list.'''
numbers = [1, 2, 2, 3, 4, 2]
count = numbers.count(2)
print("Occurrences of 2:", count)

'''5.Write a program to append the items of listi to list2 in the front.'''
list1 = [7, 8, 9]
list2 = [1, 2, 3]
result = list1 + list2
print("Combined list:", result)

'''6.Write a program to insert a new item before the second element in an existing list.'''
numbers = [10, 20, 30, 40]
numbers.insert(1, 15)
print("After insertion:", numbers)

'''7.Write a program to remove the item from a specified index in a list.'''
numbers = [1, 2, 3, 4, 5]
del numbers[2]
print("After deletion:", numbers)

'''8.Write a program to remove the first occurrence of a specified element from a list.'''
numbers = [4, 5, 6, 5, 7]
numbers.remove(5)
print("After removing first occurrence of 5:", numbers)
