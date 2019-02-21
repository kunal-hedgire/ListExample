'''
#missing number
def missing_number(A):
    n=len(A)
    total=(n+1)*(n+2)/2
    sum_A=sum(A)
    return total - sum_A
A=[1,2,3,4,5,7,8,9,10]
miss = missing_number(A)
print(miss)
'''
'''
#finding missing with duplicate
def missing_duplicate(arr,size):
    for i in range(size):
        if arr[abs(arr[i]) - 1] > 0:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
        else:
            print("The repeating element is", abs(arr[i]))

    for i in range(size):
        if arr[i] > 0:
            print("and the missing element is", i + 1)

# Driver program to test above function */
arr = [3,4,5,6,2,1,9,9,8]
n = len(arr)
missing_duplicate(arr, n)
'''
'''
#not is attached to done
def deco2(func):
    def inner():
        print("not")
        func()
    return inner

@deco2
def deco3():
    print("done")

deco3()

#without using conditions statement count
lis1=[0,1,1,0,1,1,0,0,0]
a=0
for i in lis1:
    a=a+i
print(a)

#reverse a string without using any in built function
str='hello world'
count=0
for i in str:
    a=str[len(str)-1-count]
    count+=1
    print(a)
    
#one key to many value in list
d={'x':'randy','y':'slice','z':'randy'}
d2={}
for i,j in d.items():
    if j in d2:
       d2[j]= list(d2[j])+[i]
    else:
        d2[j]=i
print(d2)
'''
'''
#convert two list into one dict
import itertools
list1=[1,2,3,4,5,6,7]
list2=[10,20,30,40,5,60,65,15]
d1=dict(itertools.zip_longest(list1,list2))
print(d1)

list1=[1,2,3,4,5,6,7]
list2=[10,20,30,40,5,60,65,15]

d1=dict(zip(list1,list2))
print(d1)
print('*'*40)

#histogram
def histo(items):
    for i in items:
        output=''
        times=i
        while (times > 0):
            output +='@'
            times-=1
        print(output)
histo([5,4,3,2,1,1,2,3,4,5])
'''
'''
#can't sort
#iterate only one

list1=[2,5,17,12,31,6,41,35]
def func1(l):
    if l[0] > l[1]:
        max1 = l[0]
        max2 = l[1]
    else:
        max1 = l[1]#5
        max2 = l[0]#2

    for i in range(2,len(l)):
        if max2 < l[i]:
            if max1 < l[i]:
                max2=max1
                max1=l[i]
            else:
                max2=l[i]
    return (max1,max2)

print(func1(list1))


#large file divided into chunks

def read_large_file(file_handler, block_size=10000):
    block = []
    for line in file_handler:
        block.append(line)
        if len(block) == block_size:
            yield block
            block = []

    # don't forget to yield the last block
    if block:
        yield block


with open('') as file_handler:
    for block in read_large_file(file_handler):
        print(block)
'''






















