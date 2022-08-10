
# global variable
c = 0
def add():
    global c
    c = c + 2 # increment by 2
    print("Inside add():", c)

add()
print("In main:", c)

# lobal variable
def fn():
                a=20
                b=30
                print(a+b)