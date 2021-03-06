'''
#protoType Design pattern
from abc import ABC
import copy


class Emp(ABC):

    def __init__(self,id,name,age):
        self.empId = id
        self.empName = name
        self.empAge = age


class PEmp(Emp):
    def __init__(self,id,nm,age):
        super().__init__(id,nm,age)

    def __str__(self):
        return 'PEmp Id : {}, Name : {}, Age : {}'.format(self.empId,self.empName,self.empAge)

class CEmp(Emp):
    def __init__(self,id,nm,age):
        super().__init__(id,nm,age)

    def __str__(self):
        return 'CEmp Id : {}, Name : {}, Age : {}'.format(self.empId,self.empName,self.empAge)


class EmpFactory :

    @classmethod
    def getEmpInstance(cls,obj):
            return copy.deepcopy(obj)


p1 = PEmp(10,"A",28)
p2 = EmpFactory.getEmpInstance(p1)

print(p1)
print(p2)

p3 = CEmp(11,"B",29)
p4 = EmpFactory.getEmpInstance(p1)

print(p3)
print(p4)



p1.empAge = 100
p3.empAge = 300
p4.empAge = 400

print(p1) # 100
print(p2)
print(p3)
print(p4) #300
'''

from abc import ABC
import copy


class Emp(ABC):
    def __init__(self,id,nm,age):
        self.empid=id
        self.empName=nm
        self.empage=age

class CEmp(Emp):
    def __init__(self,id,nm,age):
        super().__init__(id,nm,age)

    def __str__(self):
        return 'CID:{},CName:{},CAge:{}'.format(self.empid,self.empName,self.empage)


class PEmp(Emp):
    def __init__(self,id,nm,age):
        super().__init__(id,nm,age)

    def __str__(self):
        return 'PID:{},PName:{},PAge:{}'.format(self.empid,self.empName,self.empage)

class EmpFactory:
    @classmethod
    def getinstance(cls,obj):
        return copy.deepcopy(obj)


c=CEmp(1,'kunal',25)
c1=EmpFactory.getinstance(c)

print(c)
print(c1)

p=PEmp(2,'abc',30)
p1=EmpFactory.getinstance(p)

print(p)
print(p1)

c.empage=56
print(c)
print(c1)


'''
print(c)
print(c1)


p=PEmp(2,'abc',30)
p1=EmpFactory.getinstance(p)

print(p)
print(p1)

c.empage=56
print(c)

'''














