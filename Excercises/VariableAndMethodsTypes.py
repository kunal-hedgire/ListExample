#1.Static vs instance
class Test:
    x=10
    def __init__(self):
        self.y=20
t=Test()
t1=Test()
print(t.x,t.y)
Test.x=30
t1.y=40
print(t1.x,t1.y)
print(t.x,t.y)
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%GAP%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
#2.Static Declaration
class StatticExample:
    oc=10
    def __init__(self):
        StatticExample.ic=20
    def met(self):
        StatticExample.im=30

    @classmethod
    def m1(cls):
        cls.d1=40
        StatticExample.d2=50

    @staticmethod
    def m2():
        StatticExample.sv=60

print(StatticExample.__dict__)
t=StatticExample()
t.m1()
print(StatticExample.__dict__)
t.met()
print(StatticExample.__dict__)
t.m2()
print(StatticExample.__dict__)

print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%GAP%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
#3.Access Static variables
class StatticExample:
    oc=10
    def __init__(self):
        print(self.oc)
    def met(self):
        print(self.oc)

    @classmethod
    def m1(cls):
        print(cls.oc)

    @staticmethod
    def m2():
        print(StatticExample.oc)

t=StatticExample()
print(StatticExample.oc)
print(t.oc)
t.m1()
t.met()
t.m2()




