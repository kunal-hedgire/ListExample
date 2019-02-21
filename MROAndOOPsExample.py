'''
#1St Example of MRO
class A:
    def whereiam(self):
        print('in class A')

class B:
    def whoiam(self):
        print("i am method")


class C(A,B):
    pass


c=C()
print(dir(c))
print(c.whereiam)
print(c.whoiam)

class F(object): pass


class E(object): pass


class D(object): pass


class C(D,F): pass


class B(D,E): pass


class A(B,C): pass


print(C.mro())
'''
#%%%Instance variables%%%%
# 1]declare inside constructor
#OOPS Concepts
'''
class emp:
    def __init__(self,nm,age,add):
        self.name=nm
        self.age=age
        self.address=add


e=emp('kunal',11,'pune')
print(e.__dict__)

#2]declare inside instance method
class Test:
    def __init__(self):
        self.a=10
        self.b=20
    def m(self):
        self.c=30

t=Test()
t.m()
print(t.__dict__)

#3]declare outside of the class by using object reference variables
class Test2:
    def __init__(self):
        self.a=10
        self.b=20
    def m(self):
        self.c=30
t=Test2()
t.m()
t.d=40
print(t.__dict__)

#4.How to access instance variable
class Test3:
    def __init__(self):
        self.a=10
        self.b=20
    def display(self):
        print(self.a)
        print(self.b)

t=Test3()
t.display()
print(t.a,t.b)

#5.How delete instance varible from a object
#1.Within The class we can delete instance variable
#2.From outside the class
class Test4:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40
    def delele(self):
        del self.d #from inside the class
t=Test4()
print(t.__dict__)
t.delele()
print(t.__dict__)
del t.a #from outside the class
print(t.__dict__)


class test:
    def __init__(self):
        self.a = 10
        self.b = 20

t1=test()
t2=test()
t1.a=100
t1.b=200
print(t1.a,t1.b)
print(t2.a,t2.b)
'''
'''
#2.Static variable
class STest:
    x=10
    def __init__(self):
        self.y=20
s1=STest()
s2=STest()
print(s1.x,s1.y)
print(s2.x,s2.y)
STest.x=100
s1.y=200
print(s1.x,s1.y)
print(s2.x,s2.y)

#Various Place to declare static varible
class STest1:
    a=10 #declare directly
    def __init__(self):
        STest1.b=20#inside constructor by using class name

    def m1(self):
        STest1.c=40#Inside instance method by using class name

    @classmethod
    def m2(cls):
        cls.d=50#inside class method by using either class name or cls variable

    @staticmethod
    def m3():
        STest1.e=60#Inside static method by using class name

print(STest1.__dict__)
s=STest1()
print(STest1.__dict__)
s.m1()
print(STest1.__dict__)
STest1.m2()
print(STest1.__dict__)
STest1.m3()
print(STest1.__dict__)

#Where can we modify the value of static variable
class modify:
    a=777
    @classmethod
    def m1(cls):
        cls.a=888

    @staticmethod
    def m2():
        modify.a=999

print(modify.a)
modify.m1()
print(modify.a)
modify.m2()
print(modify.a)

#changes the value of static variable by using either self or object reference variables
class change:
    a=10
    def m1(self):
        self.a=20
c=change()
c.m1()
print(change.a)
print(c.a)
'''
'''
#3.Local variables
class LocalDemo:
    def m1(self):
        a=100
        print(a)
    def m2(self):
        b=200
        print(b)
        #print(a) #can not access a local variable from outside the method 
l=LocalDemo()
l.m1()
l.m2()
'''
'''
#%%%%%%%%%%%%%%%%%%%%%%%% METHODS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#1.Instance method using getter and setter

class Stud:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setMarks(self,mark):
        self.mark=mark
    def getMark(self):
        return self.mark

n=input("enter the no students")
for i in range(len(n)):
    s=Stud()
    name=input("Enter Name")
    s.setName(name)
    mark=input("Enter marks")
    s.setMarks(mark)
    print('HI',s.getName())
    print('Your marks is:',s.getMark())
'''
'''
#2.class method
class Animal:
    legs=4
    @classmethod
    def m1(cls,name):
        print('{} walks with {} legs '.format(name,cls.legs))

Animal.m1('Dogs')
Animal.m1('Cat')
'''
'''
#3.Static Method\

class MathDemo:
    @staticmethod
    def m1(x,y):
        print('the sum is:',x+y)

    @staticmethod
    def m2(x,y):
        print('the product',x*y)

    @staticmethod
    def m3(x,y):
        print('the avg',(x+y)/2)

MathDemo.m1(10,20)
MathDemo.m2(5,5)
MathDemo.m3(10,5)
'''
'''
#Inner classes
class Outer:
    def __init__(self):
        print('inside outer class')
    def m2(self):
        print("Inside m2 method")

    class Inner:
        def __init__(self):
            print("inside Inner class")
        def m1(self):
            print("inside m1 method")


o=Outer()
i=o.Inner()
i.m1()
o.m2()
'''
'''
#Destructor
import time
class Test7:
    def __init__(self):
        print("object init")
    def __del__(self):
        print("object ready to die")

t1=Test7()
t1=None
time.sleep(5)
print("End of application")
'''
'''
#find number of references of objects
import sys
class PASS:
    pass

t1=PASS()
t2=t1
t3=t1
t4=t1
print(sys.getrefcount(t1))
'''
'''
#Operator Overloading (+)
class add:
    def __init__(self,page):
        self.page=page

    def __add__(self, other):
        return self.page+other.page

b1=add(100)
b2=add(200)
print("the total number of pages is:",b1+b2)

#Overloading > and <= operator
class Students:
    def __init__(self,name,marks):
        self.name=name
        self.mark=marks
    def __gt__(self, other):
        return self.mark>other.mark
    def __le__(self, other):
        return self.mark<=self.mark
print('10>20=',10>20)
s1=Students('kunal',99)
s2=Students('Shraddha',85)
print("s1>s2=",s1>s2)
print("s1<s2=",s1<s2)
print("s1<=s2=",s1<=s2)
print("s1>=s2=",s1>=s2)

#Overload (*)
class Emp:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def __mul__(self, other):
        return self.sal*other.day

class TimeSheet:
    def __init__(self,name,day):
        self.name = name
        self.day = day

e=Emp('kunal',500)
t=TimeSheet('kunal',30)
print("THe month salary is",e*t)
'''
'''
#Method Overloading
class TEST:
    def sum(self,*a):
        total=0
        for i in a:
            total=total+i
        print('The sum is:',total)


t=TEST()
t.sum(10,20)
t.sum(10,20,30)
t.sum(10,20,30,40)
'''
'''
#constructor overloading
class ConTest:
    def __init__(self):
        print("no args cons")

    def __init__(self,a):
        print("one args cons")

    def __init__(self,a,b):
        print("two args cons")

    def __init__(self):
        print("no args cons")
t1=ConTest()
'''
'''
#Method Overriding
class P:
    def property(self):
        print("Gold+Land+Cash+Power")
    def marry(self):
        print('rrr')
class C(P):
    def marry(self):
        super().marry()
        print("Shraddha SAP Wali")

c=C()
c.property()
c.marry()

#Method Overriding
class P:
    def __init__(self):
        print("Base Class cons")
class Q(P):
    def __init__(self):
        #super().__init__()
        print("child class cons")

q=Q()
'''






































































































































































































































































































































































