'''
#1.get the input string and print it
def fun1():
    str =input('enter the string:')
    if str:
        print(str.upper())
    else:
        raise Exception ('string is empty')

    #for i in range(0,len(str)):

fun1()
'''
'''
#2.Write a program that accepts a sequence of whitespace separated words as input and prints the words after
# removing all duplicate words and sorting them alphanumerically.
def removeandsort(str):
   str=str.split()
   s = set(str)
   print(sorted(s))
   #for i in range(0,str):
in1 = input('enter the string:')
a=removeandsort(in1)
#print(a)
'''
'''
#3.Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not.
#  The numbers that are divisible by 5 are to be printed in a comma separated sequence.
value = []
items=[x for x in input('Enter the binary 4 digits numbers:').split(',')]
for p in items:
    intp = int(p, 2)
    if intp%5==0:
        value.append(p)

print(','.join(value))
'''
'''
#4.Write a program, which will find all such numbers between 1000 and 3000 (both included) such that
# each digit of the number is an even number.
#The numbers obtained should be printed in a comma-separated sequence on a single line.
values=[]
for i in range(1000,3001):
    if i%2==0:
        values.append(i)
print(' '.join(str(values)))
'''
'''
#5.Write a program that accepts a sentence and calculate the number of letters and digits
import re
str='hello world 123'
d={'DIGIT':0,'LETTER':0}
for i in str:
    if i.isdigit():
        d['DIGIT']+=1
    elif i.isalpha():
        d['LETTER']+=1
    else:
        pass
print(d)
'''
'''
#6.Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
str='Hello World'
d = {'UPPER':0,'LOWER':0}
for i in str:
    if i.isupper():
        d['UPPER']+=1
    elif i.islower():
        d['LOWER']+=1
print(d)

#7.Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

a = input('Enter The number:')
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
print (n1+n2+n3+n4)
'''
'''
#8.Use a list comprehension to square each odd number in a list. The list is input
#  by a sequence of comma-separated numbers.
s=input('Enter the numbers:')
s1=[x for x in s.split(',') if int(x)%2!=0]
print(','.join(s1))
'''
#9.Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:
netamount = 1000
log=input('Enter the log:')
#values = log.split(' ')

for i in log.split(','):
    print(i)
    ops = i[0]
    amt=1
    #amt = int(i[1])
    if ops == 'D':
        netamount +=amt
    elif ops == 'W':
        netamount-=amt
    else:
        pass
print(netamount)















