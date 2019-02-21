list1=[55,30,858,988,44]
list4=[10,55,88]

'''
#relational operator on list
print(list1 < list4)
print(list1 > list4)
#list comparison operator
print(list1 == list4)
print(list1 != list4)

#clear list
print(list1)
list1.clear()
print(list1)
#list concatination with +
#list3=[10,20]
#c=list1+list3
#print(c)

#cloning of list
print(list1)
x=list1.copy()
x[1]=10
print(x)
y=list1
print(id(y))
print(id(list1))

#list reverse by nature
list1.sort()
print(list1)
list1.sort(reverse=False)
print(list1)
list1.sort(reverse=True)
print(list1)

#list sort()
list1.sort()
print(list1)

#list reverse
print(list1)
list1.reverse()
print(list1)
#list append
list1.append('A')
list1.append('B')
list1.append('C')
print(list1)

#list insert

list2=[]
list2.insert(0,'a')
list2.insert(1,'b')
print(list2)

#list extend or concetenation
list1.extend(list2)
print(list1)

#list remove and pop

list1.remove('A')
print(list1)
#print('A' in list1)
print(list1.pop())
print(list1)
'''