'''
class Point3D(object):
    def __init__(self,a,b,c):
        self.x = a
        self.y = b
        self.z = c
    def __repr__(self):
        return "Point3D(%d, %d, %d)" % (self.x, self.y, self.z)
    def __str__(self):
        return repr(self)
            #"(%d, %d, %d)" % (self.x, self.y, self.z)
my_point = Point3D(1, 2, 3)
print (my_point) # __repr__ gets called automatically
print (my_point) # __str__ gets called automatically
'''
'''
s='Hello Python'
print(str(s))
print(str(10/2))
'''
'''
import datetime
today=datetime.datetime.now()
print("str()")
print(str(today))
print("repr()")
print(repr(today))
'''
from datetime import date
class info:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def from_birth_year(cls,name,year):
        return cls(name,date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18


p1=info('kunal',21)
p2=info.from_birth_year('kunal',1993)

print(p1.age)
print(p2.age)
print(p1.isAdult(20))


























