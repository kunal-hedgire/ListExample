'''Checking the greater number
while True:
    try:
        num1 = int(input("Enter 1st number"))
        num2 = int(input("Enter 2nd number"))

        if num1 <= 0 or num2 <= 0:
            print("not a correct input")

        elif num1 < num2:
            print("1st number is greater")
            break

        elif num1==num2:
            print("both is equal")
            break

        else:
            print("2nd number is greater")
            break

    except:
        print("Your not giving correct value")
'''
'''Three number greater'''
'''
print("three number comparison \n")

try:
    num1 = int(input("Enter 1st number"))
    num2 = int(input("Enter 2nd number"))
    num3 = int(input("Enter 3nd number"))

    if num1 <= 0 or num2 <= 0 or num3 <=0:
        print("")
except:
    print("not a correct input")
else:
    if num1 > num2 or num1 > num3:
        print("num1 number is greater")

    elif num2 > num3:
        print("num2 is greater")

    elif num1 == num2 == num3:
        print("all is equal")

    else:
        print("num3 is greater")
'''
'''
#sorting list without using built in function
list1=[30,20,10]
for i in range(list1.__len__()):
    for j in range(list1.__len__()):
        if list1[i]<list1[j]:
            list1[i], list1[j] = list1[j], list1[i]

print(list1)
'''
'''
# how to remove duplicate from list
def rev(duplicate):
    first=[]
    for i in duplicate:
        if i not in first:
            first.append(i)
    print(first)


rev(duplicate=[1,1,1,2,2,5,5,])

#names = [‘john’, ‘fan’, ‘sam’, ‘megha’, ‘popoye’, ’tom’, ‘jane’, ‘james’,’tony’]
names=['john','fan','sam','megha','popoye','tom','jane','james','tony']

a=[ name for name in names if name[0]=='j'.lower()]
print(a)

'''
'''
#a range from 2000 to 3200 which is divide by 7 but not multitply by 5
l=[]
for i in range(2000,3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))
print(',\n'.join(l))
'''
'''
#factorial

def fact(x):
    if x==0:
        return 1
    return x*fact(x-1)

x=int(input("Enetr the number"))
print(fact(x))
'''
'''
#factorial

num=int(input("enter the number"))#10

n1=0
n2=1
count=0
if num < 0:#10 < 0
    print("Enter greater than 0")
elif num==0:
    print("fact of 0 is 1")
else:
    print("Fabo series")
    while count <= num:#1<=10
        print(n1,end=',')#0,1
        nth=n1+n2#1+1=2
        n1=n2#exchange value n1=1
        n2=nth#n2=1
        #count+=1
        count=count+1# count = 1
'''
'''
#prime
num=int(input("enter the number"))

if num > 1:
    for i in range(2,num):
        if num%i==0:
            print("not prime")
            break
    else:
        print("prmie")
else:
    print("not prime")
'''
'''
#[2:4,3:9]
num=int(input("enter the number"))

d={}

print(type(d))

for i in range(1,num+1):
    d[i]=i*i

print(d)
'''
'''
num=input("enter the number")
list1=[num]
print(list1)
t=tuple(list1)
print(t)
l=num.split(",")
t=tuple(l)
print (l)
print (t)
'''
'''
#write a class with two method to get and print the string another method with upper letter
class getandprintstr:
    def __init__(self):
        self.str1=''
    def getstring(self):
        self.str1=input("Enter the string")

    def printstring(self):
        print(self.str1.upper())


obj=getandprintstr()
obj.getstring()
obj.printstring()
'''
'''
#print * right angel triangle
n=int(input("Enter the number:"))

for i in range(1,n+1):
    print(''*(n-i),end='')
    print('*'*i)
    34,67,55,33,12,98
'''
'''
n=int(input("Enter the number:"))
for num in range(2,n):#n=5
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       print (num)
'''
'''
#finding all files in folder
import os
#os.chdir("C:\PythonProjects\ListExample")
for file in os.listdir("C:\PythonProjects\ListExample"):
    if file.endswith('.txt'):
        print(os.path.join("C:\PythonProjects\ListExample", file))
'''
'''
list1=[10,20,30]
itr=iter(list1)
while True:
    try:
        element=next(itr)
        print(element)
    except:
        break
'''
#one decorator to a function
'''
def fun1(func):
    print("%"*30)
    def innerfun():
        print()
        print(" "*10,"hello")
        func()
    return innerfun
@fun1
def fun2():
    print("$"*30)


a=fun2()
#print(a)
'''
#multiple decorator to function
def fun1(func):
    def inner():
        print("deco 1")
        func()
    return inner

def fun2(func):
    def inner():
        print("deco 2")
        func()
    return inner
@fun1
@fun2
def fun3():
    print("fun3")
print(fun3())











