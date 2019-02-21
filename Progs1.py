#FAB SERIES
'''
nterms =int(input("How many terms?->"))

n1=0
n2=1
count=0

if nterms < 0:
    print("plz pass more than zero",nterms)


elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)

else:
    print("Fibonacci sequence upto", nterms, ":")
    while count <= nterms:#1 <=10 true
        print(n1,end=',')#0,
        nth = n1+n2#nth=0+1=1
        n1=n2#1
        n2=nth#1
        count +=1#1


#EVEN ODD

num=int(input("Enter the number"))

if num %2==0:
    print(num,"is even")
else:
    print(num,"is odd")

#1] Reverse String

s = input("Enter The string:")
#s='hello'
str=""
for d in s:
    str= d+str
    print(str)
print("-------------")
print(str)

#2 Reverse string

s= input("Enter the string::")
print(s[::-1])

#3]reverse string
s=input("Enter the String")
print(''.join(reversed(s)))

#4]reverse string
s=input("Enter The String:")
print(len(s))
i=len(s)-1
str=''

while i>=0:#1>=0
    str=str+s[i]
    i=i-1
    print(str)

import calendar

yy=int(input("Enter the year"))
mm=int(input("Enter the month"))

print(calendar.month(yy,mm))

#Exchange of string
s=input("Enter The String ")
spl=s.split()

l1=[]

i=len(spl)-1#2-1=1 last string of whole string

while i>=0:#i=1/true
    l1.append(spl[i])#currently pointing value of i append to L1 list
    i=i-1#i dec
output=''.join(l1)#give the sqe of string to output
print(output)


#Factorial of number
num=int(input("Enter The Number"))#7

Fact=1

if num <0:#7<0/False
    print("Plz Enter greater than 0 number")
elif num == 0:#7==0/False
    print("Fact of 0 is 1")
else:#True
    for i in range(1,num+1):
        Fact=Fact*i#F=5020 i=7
        
        print(Fact)

#Find digit in string

s=input("Enter The String")
c=0

for i in s:
    if i.isdigit():
        c +=i
print(c)


#addition of date
mnthdict={1:['jan','31'], 2:['feb','28']}
s=input("Enter The Date")#22-02-2018
datelist=s.split('-')

datelist=[int(i) for i in datelist]
days=0
for m in range(1,datelist[1]):
    days += mnthdict[m][1]
days=days+datelist[0]

if datelist[2] % 4==0 and (datelist[1]>2 or (datelist[0]==29 and datelist[1]==2)):
    days+=1
print(days)

#table
num=int(input("Enter the number"))

#num=10

for p in range(1,11):
    print(num*p)

num=int(input("Enter the number->"))

if num > 1:

    for i in range(2,num):
        if num %i == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
      print(num,'is prime')

else:
    print(num,'is not prime')
'''
'''
def arerot(str1,str2):
    size1=len(str1)
    size2 = len(str2)
    temp =''

    if size1 == size2:
        return 0

    temp=str1+str1

    if(temp.count(str2)>0):
        return 1
    else:
        return 0

str1='AACD'
str2='ACDA'
if arerot(str1,str2):
    print('str rotate')
else:
    print('not rotate')
'''

'''
def rotate(input, d):

    Lfirst = input[0: d]
    Lsecond = input[d:]
    Rfirst = input[0: len(input) - d]
    Rsecond = input[len(input) - d:]

    # now concatenate two parts together
    print("Left Rotation : ", (Lsecond + Lfirst))
    print("Right Rotation : ", (Rsecond + Rfirst))

if __name__ == "__main__":
    input = 'HHDDDD'
    d = 2
    rotate(input, d)

'''
'''
#find the digit in string with re
import re
num=input("Enter The String with Number")
l=re.findall("[0-9]+",num)
print(l)
sum=0
for i in l:
    sum+=int(i)
print(sum)
'''

'''
#Find digit in string

s=input("Enter The String")
c=0

for i in s:
    if i.isdigit():
        c +=int(i)
print(c)
'''
'''
M=[a for a in range(0,11) if a%2==0]
print(M)

#ARMSTRONG NUMBER
num=int(input("Enter The Number"))
order = len(str(num))
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   print(digit)
   sum += digit ** order
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
'''

'''
#Sorting Algorithm
list1=['1','5','6','7']
list2=[int(i)for i in list1]
list2.sort()
print(list2)

list3=[1,2,3,4]
print(list3.pop(-1))

print(list3)

print(type('defult string'))
print(type(b'defult string with b'))
'''











































