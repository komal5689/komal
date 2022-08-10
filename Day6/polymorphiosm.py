
'''Polymorphism.....'''
l=[10,20,30,40]
print(len(l))
s="welcome"
print(len(s))

'''overloading.......'''
class Ws:
    def displayinfo(self,name=''):
        print("welcome to python class A" +name)
obj=Ws()
obj.displayinfo()
obj.displayinfo('python')

'''overriding......'''
class Ws:
    def displayinfo(self):
        print("welcome to python class A")
class IIP(Ws):
    def displayinfo(self):
        super().displayinfo()
        print("welcome to IIP")
obj=IIP()
obj.displayinfo()
