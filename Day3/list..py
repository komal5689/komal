'''create a list'''
thislist = ["apple", "banana", "cherry"]
print(thislist)


# access element from list
'''Print the last item of the list:'''
thislist = ["apple", "banana", "cherry"]
'''Print the second item of the list:'''
print(thislist[1])
print(thislist[-1])
'''Return the third, fourth, and fifth item:'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


# Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


# Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


# Add Items
# the append() method:
'''To add an item to the end of the list, use the append() method:'''
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# extend() method.
'''To append elements from another list to the current list, use the extend() method.'''
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# extend() method.
# Remove Specified Item
# remove()
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index
# pop()
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
# The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist


# Clear the List
#  Clear()
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

