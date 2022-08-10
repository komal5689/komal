# create a set
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# type()
myset = {"apple", "banana", "cherry"}
print(type(myset))


# Access Items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# add()
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#remove()
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset) 