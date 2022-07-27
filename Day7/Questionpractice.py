# Using for loop

l = ['m', 'n']
n = 3
new_l=['{}{}'.format(x,y) for y in range(1,n+1) for x in l]
print(new_l)

# output ['m1', 'n1', 'm2', 'n2', 'm3', 'n3']

# ......3.....................................................................................................
l = [1, 2, 3, 0, 1, 4, 5, 2, 3]
new_l = []
for i in l:
    if i not in new_l:
        new_l.append(i)

print(new_l)
# o/p'''[1, 2, 3, 0, 4, 5]'''
# ...................2........................................................................................

l=[[4,5,3],[6,2,7],[3,2,1]]
res=[]
for i in range (0,len(l[0])):
    sum=0
    for j in range (0,len(l)):
        sum=sum+l[i][j]
    res.append(sum)

print(res)


# '''''4'''
# input the maximum number to
# which you want to send
max_num = 3000

# starting numbers from 0
n = 1200

# run until it reaches maximum number
print("Numbers divisible by 4 and 8 but not divisible by 6")
while n <= max_num:

    # check if number is divisible by 2 and 3
    if n % 4 == 0 and n % 8 == 0 and n % 6 != 0:
        print(n)

    # incrementing the counter
    n = n + 1
    # o/p
    '''Numbers divisible by 4 and 8 but not divisible by 6
    1208
    1216
    1232
    1240
    .
    .
    .
    .
    2992'''