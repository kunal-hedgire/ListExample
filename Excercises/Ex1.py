'''
Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are!
 output like this
'''
#print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\t How I wonder what you are!")
'''
#current version of python
import sys
print(sys.version)
print('=============================================')
#Current date and time
import datetime

now=datetime.datetime.now()
print('current time and date')
print(now.strftime('%Y-%m-%d %H:%M:%S'))

print('=============================================')
'''
'''
#Write a Python program which accepts the radius of a circle from the user and compute the area.
import math
r=float(input("Enter the radius of circle"))

Area=math.pi*r*r
print(Area)

print('=============================================')
'''
'''
#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them

name=input("Enter the Full Name: ")
print(name[::-1])
'''
'''
#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
#3, 5, 7, 23

val=input("enter the number of values")

list=val.split(',')
tuple=tuple(list)
print(list)
print(tuple)
'''

'''
#Write a Python program to accept a filename from the user and print the extension of that.

filename=input('Enter the fileName')

filename1=filename.split('.')

print('Extension is :',repr(filename1[-1]))
'''
'''
#Write a Python program to display the first and last colors from the following list
color_list = ["Red","Green","White" ,"Black"]

print(color_list[0],color_list[-1])
'''
'''
# Write a Python program to display the examination schedule. (extract the date from exam_st_date)
val=(11,12,2018)
print( "The examination will start from : %i / %i / %i"%val)
'''
'''
#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)
'''
'''
#Write a Python program to print the calendar of a given month and year.
import calendar
y=int(input("Enter the year:"))
m=int(input("Enter the month:"))

print(calendar.month(y,m))
'''
'''
#Write a Python program to calculate number of days between two dates.
from datetime import date

f_date=date(2018,8,20)
l_date=date(2018,9,20)


delta=l_date-f_date

print('days is:',delta.days)
'''
'''
#Write a Python program to get the the volume of a sphere with radius 6.
pi = 3.1415926535897931
r= 6.0
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)
'''
'''
#Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

def diff(n):
    if n < 17:
        return 17-n
    if n > 17:
        return (n-17)*2

print(diff(22))
print(diff(14))
'''
'''
#Addition of three number

a=int(input("Enter The First Number"))
b=int(input("Enter The Second Number"))
c=int(input("Enter The Third Number"))
if a == b == c:
    d=(a+b+c)*3
    print(d)
else:
    d = (a + b + c)
    print(d)
'''
'''
#starting la Is asel tr return string unchanged nasel tr is laun return kara
#Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given 
# string already begins with "Is" then return the string unchanged.

def att(str):
    if len(str) >=2 and str[:2]=='Is':
        return str
    return 'Is'+str
print(att('Iskunal'))
print(att('hai'))
'''
'''
#Write a Python program to get a string which is n (non-negative integer) copies of a given string.
def larger_string(str, n):
   result = ""
   for i in range(n):
      result = result + str
   return result

print(larger_string('abc', 2))
print(larger_string('.py', 3))

st=input("enter the string")
n=int(input('how many time to rotate it:'))
print(st*n)
'''
'''
# Write a Python program to count the number 4 in a given list
list=[4,4,4,42,2,2,2]
c=0
for i in list:
   if i==4:
       c+=1
print(c)
'''
'''
#Write a Python program to check whether a specified value is contained in a group of values.
def is_group_member(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))
'''
'''
#Write a Python program to print all even numbers from a given numbers list in the same order and stop 
#the printing if any numbers that come after 237 in the sequence
numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]

for i in numbers:
    if i==237:
        print(i)
        break
    elif i%2==0:
        print(i)
'''
'''
#vowel or not

st=input("Enter The String")
v=['a','e','i','o','u']
if st in v:
    print('Vowel')
else:
    print("NO Vowel")
'''

#Write a Python program to create a histogram from a given list of integers.
'''
@@
@@@
@@@@@@@
@@@@@@
is called histogram


def histogram(items):
    for n in items:
        output=''
        times=n
        while (times > 0):
            output+='@'
            times=times-1
        print(output)
histogram([2,3,4,5,6])
'''






















































































