'''inheritance'''
'''single'''
class A:
    def displayA(self):
        print("welcome to python class A")
class B(A):
     def displayB(self):
        print("welcome to python class B")
obj=B()
obj.displayA()
obj.displayB()


'''multilevel'''

class A:
    def displayA(self):
        print("welcome to python class A")
class B(A):
     def displayB(self):
        print("welcome to python class B")
class C(B):
    def displayC(self):
        print("welcome to python class C")
obj=C()
obj.displayA()
obj.displayB()
obj.displayC()

'''Multiple'''

class A:
    def displayA(self):
        print("welcome to python class A")
class B:
     def displayB(self):
        print("welcome to python class B")
class C(A,B):
    def displayC(self):
        print("welcome to python class C")
obj=C()
obj.displayA()
obj.displayB()
obj.displayC()

'''herarichal'''
class A ():
    def f1(self):
        print('A')
class B(A):
    def f2(self):
        print('B')
class C(B):
    def f3(self):
        print('C')
ob=C()
ob.f1()
ob.f3()

'''hybrid'''
class School:
    def func1(self):
        print("This function is in school.")
 
 
class Student1(School):
    def func2(self):
        print("This function is in student 1. ")
 
 
class Student2(School):
    def func3(self):
        print("This function is in student 2.")
 
 
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")
 
 
# Driver's code
object = Student3()
object.func1()
object.func2()