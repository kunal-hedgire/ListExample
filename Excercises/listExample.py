'''
#1.Write a Python program to sum all the items in a list.
list1=[10,-20,30,-40]
c=0
for i in list1:
   c=i+c
print(c)
'''
'''
#2.Write a Python program to multiplies all the items in a list.
list1=[10,20,30,40]
c=1
for i in list1:
    c=c*i
print(c)
'''
'''
#3.Write a Python program to get the largest number from a list.
list1=[40,50,10,30]
max=list1[0]
for i in list1:
    if i > max:
        max=i
prisnt(max)
'''
'''
#4.Write a Python program to get the smallest number from a list.
list1=[10,20,30,40,5]

min=list1[0]

for i in list1:
    if min < i:
        min=i
print(i)
'''
'''
#5.Write a Python program to count the number of strings where the string length is 2 or more and the first
# and last character are same from a given list of strings.

list1=["xyz","abc","aba",'1231','23452']
c=0

for i in list1:
    if len(i)>2 and i[0]==i[-1]:
        c+=1
print(c)
'''
'''
#6.Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a
# given list of non-empty tuples. Go to the editor
#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
'''
'''
#7.Write a Python program to remove duplicates from a list.
def duplicate(item):
    list1=[]
    for i in item:
        if i not in list1:
            list1.append(i)
    return list1
d=duplicate([1,2,3,4,4,1,2,3,1,2,3])
print(d)
'''
'''
#8.Write a Python program to check a list is empty or not.
list1=[10]

if not list1:
    print("List is Empty")
else:
    print("List is not empty")
'''
'''
#9.clone or copy a list
list1=[10,20,30]
print(list1)
list2=list(list1)
print(list2)
'''
'''
#10.Write a Python program to find the list of words that are longer than n from a given list of words.
def search(n,str):
    word_len=[]
    t=str.split(' ')
    for i in t:
        if len(i) > n:
            word_len.append(i)
    return word_len

s=search(3,'this fox than dog')
print(s)
'''
'''
#11-.Write a Python function that takes two lists and returns True if they have at least one common member
list1=[10,20,30]
list2=[10,50,60]

def Com(list1,list2):
    for i in list1:
        for j in list2:
            if i == j:
               return True
            else:
                return False

d=Com([10,20,30],[10,50,60])
print(d)
'''
'''
#12.Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

list1=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

list1=[x for (i,x) in enumerate(list1) if i not in(0,4,5)]
print(list1)
'''
'''
#13.Write a Python program to print the numbers of a specified list after removing even numbers from it.

list1=[10,15,14,19,22,25,26,30,33,35]

list1=[x for x in list1 if x%2!=0]

print(list1)
'''
'''
#14.Write a Python program to shuffle and print a specified list.

import random
list1=[10,20,30,40]
random.shuffle(list1)
print(list1)
'''
#15.Write a Python program to generate and print a list of first and last 5 elements where
# the values are square of numbers between 1 and 30 (both included).
'''
def printValues():
    l = list()
    for i in range(1,21):
        l.append(i**2)
    print(l[:5])
    print(l[-5:])

printValues()
'''
'''
#16. Write a Python program to generate all permutations of a list in Python.
import itertools
print(list(itertools.permutations([1,2,3])))
'''
'''
#17.Write a Python program to get the difference between the two lists.
list1=[1,2,3,4]
list2=[1,2]

print(list(set(list1)-set(list2)))
'''
'''
#18.Write a Python program access the index of a list.
list1=[10,20,30,40,50]

for i,x in enumerate(list1):
    print(i,x)
'''
'''
#19.Write a Python program to convert a list of characters into a string.
list1=['H','E','L','L','O']
str1=''.join(list1)
print(str1)
'''
'''
#20.Write a Python program to find the index of an item in a specified list.
list1=[10,20,30,40]

print(list1.index(30))
'''
#21.Write a Python program to flatten a shallow list.
'''
import itertools
original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]

new_list=list(itertools.chain(*original_list))
print(new_list)
'''
#22.one list to second list
'''
list1=[10,20,30]
list2=[40,50,60]
finallist=list1+list2
print(finallist)
'''
'''
#23.Write a Python program to select an item randomly from a list.
import random
list1=[100,200,3000,4000]
print(random.choice(list1))
'''
'''
#24.Write a python program to check whether two lists are circularly identical.
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

print('Compare list1 and list2')
print(' '.join(map(str, list2)) in ' '.join(map(str, list1*2)))
print('Compare list1 and list3')
print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))
print('compare list2 with list3')
print(' '.join(map(str,list2)) in ''.join(map(str,list3)))
'''
'''
#25.Find second smallest number in list
def second_smallest(numbers):
  if (len(numbers)< 2):
    return
  if ((len(numbers)==2) and (numbers[0] == numbers[1]) ):
    return
  dup_items = set()
  uniq_items = []
  for x in numbers:
    if x not in dup_items:
      uniq_items.append(x)
      dup_items.add(x)
  uniq_items.sort()
  return  uniq_items[1]

print(second_smallest([1, 2, -8, 2, 0,0, 2]))
'''
'''
#26.Write a Python program to find the second largest number in a list.
def second_high(numbers):
    if len(numbers) < 2:
        return
    if ((len(numbers)==2) and (numbers[0] == numbers[1]) ):
        return
    dup_item=set()
    uniq_item=[]

    for x in numbers:
        if x not in dup_item:
            uniq_item.append(x)
            dup_item.add(x)
    uniq_item.sort()
    return uniq_item[-2],uniq_item[-1]

print(second_high([10,20,50,90,10,-5,89,100]))
'''
#27.Write a Python program to get unique values from a list.
'''
def duplicate(items):
    uni=[]
    for x in items:
        if x not in uni:
            uni.append(x)
    return uni

print(duplicate([10,10,20,30,30,40,50,50,20]))

#second method with set and list

list1=[10,10,20,30,30,40,40,40,50,50,20]
my_set=set(list1)
my_list=list(my_set)
print("unique values",my_list)
'''
'''
#28.Write a Python program to get the frequency of the elements in a list.
from collections import Counter
list1=[1,1,1,1,1,2,2,2,3,3,3,3,3,4,4,4,4,4]
print(Counter(list1))
'''
'''
#29.Write a Python program to count the number of elements in a list within a specified range
list1=[10,20,30,50,60,625,6,666,656,66]
cnt=0
min=50
max=1000
for i in list1:
    if min <= i <= max:
        cnt+=1
print(cnt)
'''
'''
#30.Write a Python program to check whether a list contains a sublist.
def is_Sublist(l, s):
    sub_set = False
    if s == []:
        sub_set = True
    elif s == l:
        sub_set = True
    elif len(s) > len(l):
        sub_set = False

    else:
        for i in range(len(l)):
            if l[i] == s[0]:
                n = 1
                while (n < len(s)) and (l[i + n] == s[n]):
                    n += 1

                if n == len(s):
                    sub_set = True

    return sub_set


a = [2, 4, 3, 5, 7]
b = [4, 3]
c = [2, 5]
print(is_Sublist(a, b))
print(is_Sublist(a, c))
'''
'''
#31.Write a Python program to generate all sublists of a list.
def sub_list(items):
    subs=[[]]
    for i in range(len(items)):
        n=i+1
        while n <= len(items):
            sub=items[i:n]
            subs.append(sub)
            n+=1
    return subs

print(sub_list([10,20,30,40]))
'''
'''
#32.Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number.

def prime_eratosthenes(n):
    prime_list = []
    for i in range(2, n+1):
        if i not in prime_list:
            print (i)
            for j in range(i*i, n+1, i):
                prime_list.append(j)

print(prime_eratosthenes(100))
'''
'''
#33.Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
list1=['p','q']
n=4
new_list=['{}{}'.format(x,y) for y in range(1,n+1) for x in list1 ]
print(new_list)
'''
'''
#34.Write a Python program to find common items from two lists
list1=[10,20,30]
list2=[30,50,20]
print(set(list1)& set(list2))
'''
'''
#35.Write a Python program to change the position of every n-th value with the (n+1)th in a list.
from itertools import zip_longest, chain, tee
def replace2copy(lst):
    lst1, lst2 = tee(iter(lst), 2)
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))
n = [0,1,2,3,4,5]
print(replace2copy(n))

#36.Write a Python program to convert a list of multiple integers into a single integer.
list1=[11, 33, 50]
print(' '.join(map(str,list1)))
'''
'''
#37. Write a Python program to find common items from two lists.
list1=[10,20,30]
list2=[30,40,10]
print(set(list1) & set(list2))

#list3=[]
#for i in list1:
 #   for j in list2:
  #      if i==j:
   #        print('list1 value:',i,'=','list2 value:',j)
'''
'''
#38.Write a Python program to split a list based on first character of word.
from itertools import groupby
from operator import itemgetter

word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)
#38.Write a Python program to create multiple lists.
obj={}
for i in range(1,21):
    obj[str(i)]=[]
print(obj)
'''
'''
#39.Write a Python program to find missing and additional values in two lists.
list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']
print('Missing values in second list: ', ','.join(set(list1).difference(list2)))
print('Additional values in second list: ', ','.join(set(list2).difference(list1)))
'''
'''
#40.Write a Python program to split a list into different variables.
color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
         ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]

var1,var2,var3=color
print(var1)
print(var2)
print(var3)

#41.Write a Python program to generate groups of five consecutive numbers in a list.
l=[[5*i+j for j in range(1,6)]for i in range(5)]
print(l)
'''
'''
#42.Write a Python program to check if all dictionaries in a list are empty or not.
list1= [{},{},{}]
list2= [{1,2},{},{}]
print(all(not d for d in list1))
print(all(not d for d in list2))

#43.Write a Python program to get the depth of a dictionary.
def dict_depth(d):
    if isinstance(d, dict):
        return 1 + (max(map(dict_depth, d.values())) if d else 0)
    return 0
dic = {'a':1, 'b': {'c': {'d': {}}}}
print(dict_depth(dic))
'''
'''
#44.Write a Python program to remove duplicates from a list of lists
import itertools
num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
num.sort()
new_num=list(num for num,_ in itertools.groupby(num))
print(new_num)
'''
'''
#45.Write a Python program to find all the values in a list are greater than a specified number
list1=[200,300,58,68,123,4568,4654,899,1000]

for i in list1:
    if i >= 200:
        print(i)
'''
'''
#46.Write a Python program to remove and print every third number from a list 
# of numbers until the list becomes empty.
def Print_3rd(number):
    position=3-1
    idx=0
    len_list = (len(number))
    while len_list > 0:
        idx=(position+idx) % len_list
        print(number.pop(idx))
        len_list-=1

nums=[10,20,30,40,50,60,70,80,90]
print(Print_3rd(nums))
'''
'''
#47.printing each word from file
import collections
import pprint
#file_input = input('File Name: ')
with open('C:\PythonProjects\ListExample\HISTORYlistener.log', 'r') as info:
  count = collections.Counter(info.read().upper())
  value = pprint.pformat(count)
'''
#48.
'''
#zip() function is used to map similar index of multiple conatainer.

name = ['kunal','shraddha','priyanka']
roll_no = [10,5,6]
marks = [68,68,70]
a=zip(name,roll_no,marks)
b=list(a)
print("zipping value ",b)
print('\n')

n,r,m = zip(*b)
print('the unzipped process')
print(n)
print(r)
print(m)
'''






























































































































































































