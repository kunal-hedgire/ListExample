'''#1.Ascending order by keys
import operator
dic={'A':1,'D':0,'C':3,'B':2}

print(dic)
sorted_d=sorted(dic.items(),key=operator.itemgetter(0))
print(sorted_d)
sorted_d1 = sorted(dic.items(), key=operator.itemgetter(0),reverse=True)
print(sorted_d1)
print("*******************************************")
'''
'''
#2. Write a Python script to add a key to a dictionary.
dict1={0:10,2:20}
dict1.update({3:30})
print(dict1)
'''
'''
#3.Write a Python script to concatenate following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic1.update(dic2)
dic1.update(dic3)
print(dic1)
'''
'''
#4.Write a Python script to check if a given key already exists in a dictionary

dic1={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in dic1:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(10)
is_key_present(9)
'''
'''
#5.Write a Python program to iterate over dictionaries using for loops.
dic1={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

for x,y in dic1.items():
    print("key=",x)
    print("Value=",y)
'''
#6.Write a Python script to generate and print a dictionary that contains a number (between 1 and n)
# in the form (x, x*x).

#7.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the
# values are square of keys.
'''
num1=int(input("Enter The Number to print:"))
dic1= dict()

for i in range(1,num1+1):#for i in range(1,n+1)
    dic1[i]= i*i
print(dic1)
'''
#8.Write a Python script to merge two Python dictionaries
'''
dic1={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic2={7: 70, 8: 80, 9: 90, 10: 100, 11: 110, 12: 120}

dic1.update(dic2)
print(dic1)
'''
'''
#9.Write a Python program to iterate over dictionaries using for loops
dic1={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
for x,y in dic1.items():
    print("key=",x,"value= ",y)
'''
'''
#10.Write a Python program to sum all the items in a dictionary

dic1={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
count=0
cnt=0
for x,y in dic1.items():
    count+=x
    cnt+=y
print(count,cnt)
'''
'''
#11.Write a Python program to multiply all the items in a dictionary.
dic1={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
count=1
cnt=1
for x,y in dic1.items():
    count*=x
    cnt*=y
print(count,cnt)
'''
'''
#12. Write a Python program to remove a key from a dictionary.
dic1={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(dic1)
if 1 in dic1:
    del dic1[1]
print(dic1)
'''
'''
#13.Write a Python program to map two lists into a dictionary
list1=[1,2,3,4,5,6]
list2=[10,20,30,40,5,60]
d1=dict(zip(list1,list2))
print(d1)
'''
'''
#14. Write a Python program to sort a dictionary by key
color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}

for key in sorted(color_dict):
    print("%s: %s" % (key, color_dict[key]))
'''
'''
#15. Write a Python program to get the maximum and minimum value in a dictionary.
my_dict={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print('Maximum Value: ',my_dict[key_max])
print('Minimum Value: ',my_dict[key_min])
'''
'''
#16.Write a Python program to get a dictionary from an object's fields.
class obj(object):
    def __init__(self):
        self.x = 'Red'
        self.y = 'Green'
        self.z = 'Black'

    def my(self):
        pass

o=obj()
print(o.__dict__)
'''
'''
#17.Write a Python program to remove duplicates from Dictionary
dic1={'A':10,'B':20,'C':20,'D':30}
dic2={}
for i,j in dic1.items():
    if j not in dic2.values():
        dic2[i]=j

print(dic2)
'''
'''
#18.Write a Python program to check a dictionary is empty or not.
dic1={}

if not bool(dic1):
    print('Dict is empty')
else:
    print(dic1)
'''
'''
#19.Write a Python program to combine two dictionary adding values for common keys
import collections
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3=collections.Counter(d1)+collections.Counter(d2)
print(d3)
#for x,y in d1.items():
 #   for j,k in d2.items():
  #      if x == j:
   #        d3[x]=y+k
'''
'''
#20.Write a Python program to print all unique values in a dictionary.
d=[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

u_value = set( val for dic in d for val in dic.values())
print("Unique Values: ",u_value)
'''
'''
#21.Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
import itertools
d ={'1':['a','b'], '2':['c','d'],'3':['e','f']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))
'''
'''
#22.Write a Python program to find the highest 3 values in a dictionary
from heapq import nlargest
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
three = nlargest(3,my_dict,key=my_dict.get)
print(three)
'''
'''
#23. Write a Python program to combine values in python list of dictionaries
import collections
item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result=collections.Counter
for d in item_list:
    result[d['item']] += d['amount']
print(result)
'''
'''
#24.Write a Python program to create a dictionary from a string.
from collections import defaultdict, Counter
str1 = 'my name is yours is'
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)
'''
'''
#25.. Write a Python program to count the values associated with key in a dictionary
student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'},
 {'id': 3, 'success': False, 'name': 'Alex'}]
print(sum(d['success'] for d in student))

#26.Write a Python program to print a dictionary in table format.
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}

for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    print(*row)
'''
'''
#27.Write a Python program to convert a list into a nested dictionary of keys.
num_list=[1,2,3,4]
dic1 = current = {}
for name in num_list:
    current[name] = {}
    current=current[name]
print(dic1)
'''
'''
#28.Write a Python program to get the top three items in a shop.
from heapq import nlargest
from operator import itemgetter

items = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
for name, value in nlargest(3, items.items(), key=itemgetter(1)):
    print(name, value)
'''
'''
#29.Write a Python program to get the key, value and item in a dictionary.

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("key  value  count")
for count, (key, value) in enumerate(dict_num.items()):
    print(key,'   ',value,'    ', count)
'''
'''
#30.Write a Python program to print a dictionary line by line
students = {'Aex': {'class': 'V',
                    'rolld_id': 2},
            'Puja': {'class': 'V',
                     'roll_id': 3}}
for a in students:
    print(a)
    for b in students[a]:
        print(b, ':', students[a][b])
'''
'''
#31.Write a Python program to check multiple keys exists in a dictionary.
student = {
  'name': 'Alex',
  'class': 'V',
  'roll_id': '2'
}
print(student.keys() >= {'class', 'name'})
print(student.keys() >= {'name', 'Alex'})
print(student.keys() >= {'roll_id', 'name'})
'''
'''
#32.Write a Python program to count number of items in a dictionary value that is a list
dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
ctr = sum(map(len, dict.values()))
print(ctr)
'''
'''
#33.Write a Python program to sort Counter by value.
from collections import Counter
x = Counter({'Math':81, 'Physics':83, 'Chemistry':87})
print(x.most_common())

#34.Write a Python program to replace dictionary values with their sum.
def sum_math_v_vi_average(list_of_dicts):
    for d in list_of_dicts:
        n1 = d.pop('V')
        n2 = d.pop('VI')
        d['V+VI'] = (n1 + n2)/2
    return list_of_dicts
student_details= [
  {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
  {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
  {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
]
print(sum_math_v_vi_average(student_details))
'''
'''
#35.Write a Python program to match key values in two dictionaries.
x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
for (key, value) in set(x.items()) & set(y.items()):
    print('%s: %s is present in both x and y' % (key, value))
'''


'''
import pickle
emp={1:"A",2:"B",3:"C",4:"D",5:"E"}
file=open('emp.pickle','wb')
pickle.dump(emp,file)
file.close()
'''
'''
file1=open('C:\PythonProjects\ListExample\Excercises\emp.pickle','rb')
emp=pickle.load(file1)
print(emp)

'''
'''
'''

















































































































































