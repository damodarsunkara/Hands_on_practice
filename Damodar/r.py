import math
class shape:
     def __init__(self,area,perimeter):  
        self.area=area
        self.perimeter=perimeter
     '''method overridden'''
     def area(self):
        pass
     def perimeter(self):
        pass

class circle(shape):
    def __init__(self,radius):
        
           
            self.radius=radius

    def area(self):
        return math.pi*self.radius**2
    def perimeter(self):
        return 2*math.pi *self.radius

class Rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 *(self.length+self.breadth)
cl=circle(5)
Rea=Rectangle(34,56)
print(cl.area())
print(cl.perimeter())
print(Rea.area())
print(Rea.perimeter())

'''
print(f"area of circle:{dl.area()}, and perimeter:{cl.perimeter()}")


print(f"area of rectangle:Rea.area()}, and perimeter:{Rea.perimeter()}")
'''


         
            

