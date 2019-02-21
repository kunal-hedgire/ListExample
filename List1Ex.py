
'''
i=0
while i<len(list1):
    print("list obj",i+1)
    i=i+1
    for i in list1:
    print(i)

i=[item for item in list1]
print(i)
'''
list1=[[1,'kunal',98],[2,'kunal',65],[3,'ashish',56],[4,'kunal',48]]
names = {list1[0][1]:1}

for i in range(1,len(list1)):
    if list1[i][1] in names:
        names[list1[i][1]]=names[list1[i][1]]+1
    else:
        names[list1[i][1]]=1

print(names)