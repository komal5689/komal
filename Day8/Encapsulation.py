class Javatpoint:   
    def _init_(self, age = 0):   
         self._age = age   
      # using the getter method   
    def get_age(self):   
        return self._age   
      # using the setter method   
    def set_age(self, a):   
        self._age = a   
    
John = Javatpoint()   
    
#using the setter function  
John.set_age(19)   
    
# using the getter function  
print(John.get_age())   
    
print(John._age)