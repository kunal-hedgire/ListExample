'''
def remove(duplicate):
    frist=[]
    for num in duplicate:
        if num not in frist:
            frist.append(num)
    return frist
duplicate=[2,2,5,6,8,8,8,8,8,8,8,7,7,7,7,]
print(remove(duplicate))
'''
'''
def gen_multiplier(x):
    def multiplier(y):
        return x*y
    return multiplier

a=gen_multiplier(10)
del gen_multiplier
print(a(5))
'''
'''
class Currency:
    def __init__(self, currency_x=1):
        self.set_currency_x(currency_x)

    def currency_converter(self):
        currency_y = self.get_currency_x() * 28
        print(currency_y)
        return (currency_y)

        # implementing new getter method

    def get_currency_x(self):
        return (self.currency_x)

        # implementing new setter method

    def set_currency_x(self, currency_value):
        if currency_value < 0:
            raise ValueError("Currency can't be negative")
        self.currency_x = currency_value

num=int(input("Enter the Currency:"))
c=Currency()
c.currency_converter()
#deep copy and shallow copy
import copy
old_list=[10,20,30,[10,50]]
new_list=copy.deepcopy(old_list)

print(id(old_list))
print(id(new_list))
print("before change")
print(new_list)
print(old_list)
print("after change")
old_list[3][1]=60
print(new_list)
print(old_list)f

'''
'''
from collections import OrderedDict

dict1 = OrderedDict()
dict1['jan']=31
dict1['feb']=30
dict1['march'] = 20

OrderedDict([('jan', 31), ('feb', 30), ('march', 20)])
for key in sorted(dict1.__iter__()):
    print ("%s: %s" % (key, dict1[key]))
'''
'''
import random
list1=[10,20,3,40,0]
random.shuffle(list1)
print(list1)
random.shuffle(list1)
print("Afetr reshuffle the list",list1)
'''


class X(object):
    def __init__(self, a):
        print("x init")
        self.num = a

    def doubleup(self):
        print("doubleup")
        self.num *= 2


class Y(X):
    def __init__(self, a):
        X.__init__(self, a)

    def tripleup(self):
        print("Triple up")
        self.num *= 3


obj = Y(4)
print(obj.num)

obj.doubleup()
print(obj.num)

obj.tripleup()
print(obj.num)


