'''
num=10
def outer():
    global num
    num=20
    def inner():
        #nonlocal num
        #num=30
        print("inside inner:",num)

    print("Inside outer:", num)
    inner()


print("outside outer:",num)


outer()
'''

class Emp:
    def __init__(self,id,name):
        self.Empid=id
        self.Empname=name
    def __str__(self):
        return "Empid : {}, Empname :{}".format(self.Empid,self.Empname)
    def __eq__(self, other):
        return self.Empname == other.Empname

e1 = Emp(1,'A1')
e2 = Emp(1,'A2')
e3 = Emp(2,'A2')
e4 = e1
e5 = e4

print(e1 == e2) #False
print(e2 == e3) #True
print(e3 == e4) #False
print(e4 == e5) #True
print(e4 == e1) #True



#print(id(e1) == id(e2)) #False
#print(id(e2) == id(e3)) #False
#print(id(e3) == id(e4)) #False
#print(id(e4) == id(e5)) #True
#print(id(e4) == id(e1)) #True
