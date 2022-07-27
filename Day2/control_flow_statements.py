'''while loop'''
i = 1
while i < 6:
  print(i)
  i += 1


''' Break Statement'''
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


''' Continue Statement'''
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)



'''for loop'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

''' Break Statement'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


''' Continue Statement'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
print(x)


'''else'''
for x in range(6):
  print(x)
else:
  print("Finally finished!")



'''Nested loop'''
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


'''if elif statements'''

num = 3.4

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


