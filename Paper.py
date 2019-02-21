
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

min=0
max=0
for index,i in enumerate(list1):
    if min >i:
       if max > min:
           pass







print('#########################################################')

def ispalindrome(word):
    word1=word.lower()
    rev=word1[::-1].lower()

    if rev==word1:
        return True
    return False

print(ispalindrome('Malayalam'))

print('#########################################################')

d1={'input.txt':'randy','code.py':'stan','output.txt':'randy','A':'randy','B':'stan'}

#d2={}
#for x,y in d1.items():
 #   if y in d2:
  #      d2[y]=list(d2[y])+[x]
   # else:
    #    d2[y]=x
#print(d2)

d2={}
for x,y in d1.items():
    if y in d2:
        d2[y]=list(d2[y])+[x]
    else:
        d2[y]=x

print(d2)









