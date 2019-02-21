'''
import random
list1= ['abcd', 786 , 2.23, 'john', 70.2]
tinylist=[123,'john']
#print(list1+tinylist*2)

tuple1 = ('abcd', 786, 2.23, 'john', 70.2)
#print(tuple1)
x=[10,20,30,40,50,6,0,40,5,20,5,6,99,89,9,69,65,8,9]
del x[1]
x.remove(x)
print(x)
#random.shuffle(x)
#print(x)
#print(random.seed(3))
#print(random.randrange(50,100,2))
#print(random.choice(x))
s='123'
s2='akunal'
print(s.isalnum())
print(s.isdigit())
print(s.isnumeric())
print(s.isspace())
print(max(s))
print(s.replace('123','kunal'))
print(s2.swapcase())
'''
'''
x=[50,20,30,10]
y=[40,50,60]
#print(x.index(10))
#print(x.pop())

#a='kunalhedgire'
#print(a[:3]+a[3:])
#print(len(a))


with open('C:\PythonProjects\ListExample\Ipfile.txt','r')as file1:
    for i in file1:
         print(len(file1.readline().rstrip()))

num_strings = ['1','2','3','4','5','6']

i=[int(l) for l in num_strings]
print(i)


num_strings = [1,21,53,84,50,66,7,38,9]

odd=[i for i in num_strings if i%2==1]
even=[i for i in num_strings if i%2==0]
print('odd =',odd,'\neven=',even)


nums = [1,5,2,10,3,45,23,1,4,7,9]
nums.sort()
print(nums)

for j,k in enumerate(nums):
    print("{0}=>{1}".format(j,k))

n = [1,2,5,10,3,100,9,24]
a=[]
for i in n:
    if i>=5:
        a.append(i)
        n=a
print(a)

def func(x,*y,**z):
    print(z)
func(1,2,3)
'''

import math
#class Test:
  #  def class_method(self):
 #       print('this is a class method')

#def Moneky_fun():
 #   print('this is a monkey_fun')


#t=Test()
#t.class_method=Moneky_fun
#t.class_method()
#print(dir())

try:
    with open('Test.txt',encoding='utf-8') as file:

        file.write('HI \n')
        file.write("Bye \n")
        #print(file.tell())
        print(file.readlines())
finally:
    file.close()

