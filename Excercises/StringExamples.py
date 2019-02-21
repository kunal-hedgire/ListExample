'''
#1.Count the number of words in file
from collections import Counter
with open('C:\PythonProjects\ListExample\Excercises\Test.txt') as file:
    wordcount = Counter(file.read().split())
    for i in wordcount.items():
        print('{}\t{}'.format(*i))

#2.Count number of frequencies of alphbets
str1 = 'w3resource'
my_dict = dict()
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)

#3.count len of the string
str1 = 'w3resource'
print(len(str1))
count=0
for i in str1:
    count+=1
print(count)
print('*'*40)

#4.count the number of characters
sample = 'google.com'
d=dict()

for k in sample:
    d[k]=d.get(k,0)+1
print(d)
print('*'*40)

#5.print last 2 and first 2 digit from list and if list is less than 2 then return empty string
sample1 = 'w3w3'

if len(sample1) < 2:
    print('empty string')
else:
    print(sample1[0:2]+sample1[-2:])
    print(sample1[-1:-3])
print('*'*40)

#6.replace 2 char with $
str1 = 'restart'

char = str1[0]
str1 = str1.replace(char, '$')
str1 = char + str1[1:]
print(str1)
print('*'*40)

#7.concat the string and replace 2 element from both the list
s2 = 'abc'
s3 = 'xyz'

news2=s2[:2]+s3[2:]
news3=s3[:2]+s2[2:]
print(news2+news3)
print('*'*40)

#8.reverse
str2='who am i'
a=str2.split()
a.reverse()
print(' '.join(a))
print('*'*40)

#9.
str3 = 'abcing'
if str3[-3:] == 'ing':
    str3+='ly'
else:
    str3+='ing'
print(str3)
print('*'*40)

#10.replace the poor with good if not and poor is their
str4 = 'The lyrics is poor!'
snot=str4.find('not')
spoor=str4.find('poor')

if spoor > snot and snot > 0 and spoor > 0:
    str4=str4.replace(str4[snot:(spoor+4)],'good')
    print(str4)
else:
    print(str4)
print('*'*40)

#11.retrun the longest word
s1 = ['hi', 'this', 'is', 'python']
l=[]
for i in s1:
   l.append((len(i),i))
l.sort()
print('logest word is :',l[-1][1])
print('*'*40)

#12.remove the nth index from string
s3 = 'python'
i = int(input("Enter the index to be removed"))
first_part=s3[:i]
last_part=s3[i+1:]
print(first_part+last_part)

#13.replace 1st char with last and last char with 1st
s4 = 'python'
news4= s4[-1:]+s4[1:-1]+s4[:1]
print('after the changing words :',news4)
print('*'*40)

#15.remove the odd index of string
s5='python is'
print(s5[0::2])
print('*'*40)

#16.Occurance of each sentence
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))
print('*'*40)
'''
'''
#17.Take a input and display the string lower and upper case letter
str5 = input("Enter The string  ")
print(str5.lower())
print(str5.upper())

#18.sort
l1=['red','black','white','green','red']
l1.sort()
print(l1)
print('*'*40)

#19.create a html tag
def add_tags(tag, word):
   return "<%s>%s</%s>" % (tag, word, tag)
print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))
print('*'*40)

#20.Write a Python function to insert a string in the middle of a string.
def middle(str,word):
    return str[:2]+word+str[2:]
print(middle('{[]}','python'))
print('*'*40)
#21.
def function(str):
    return str[-2:]*4
print(function('Exercises'))
print('*'*40)
#21.if string is less than 3 then return string if not then just return 3 first letter

def ThreeLetter(str):
    if len(str) == 3:
        return str
    else:
        return str[0:3]
print(ThreeLetter('pyc'))
print('*'*40)

#22.last part of string before specified character
str1 = 'https://www.w3resource.com/python-exercises/string'
print(str1.rsplit('/', 1)[0])
print(str1.rsplit('-', 1)[0])
print('*'*40)

#23.reverse a string if len of that string is multiple of 4 of len of string
def revesrse(str):
    length = len(str)
    if length % 4 == 0:
        return ''.join(reversed(str))
    else:
        return 'the lenth of string is not multiple of len of string'
print(revesrse('python'))
print('*'*40)

#24.in a string if out of first 4 char any two is upper case then convert the whole string with upper  case
def UpperCaseStr(str):
    num=0
    for i in str[:4]:
        if i.upper() == i:
            num +=1
    if num >= 2:
        return str.upper()
    return str

print(UpperCaseStr('Python'))
print('*'*40)

#25.Lexicographically sort
def lexicographi_sort(s):
    return sorted(sorted(s), key=str.upper)

print(lexicographi_sort('w3resource'))
print(lexicographi_sort('quickbrown'))
print('*'*40)

#26.
s8 = 'python \n '
s=s8.rstrip()
print(s)
print('*'*40)

#27.Check if first char of string is strating with specified char
str5 = 'the python is very easy to learn'
print(str5.startswith('the'))
print('*'*40)
#28.{25 in w3source} Ciesear cipher

#29.print a float number with only digit
x=12.9999
y=9.1234
print("original Value x=",x,'y=',y)
print("After changes x="+'{:.2f}'.format(x))
print("After changes y="+'{:.2f}'.format(y))
print('*'*40)

#30.the following floating numbers upto 2 decimal places with a sign.
x=12.9999
y=-9.1234
print("original Value x=",x,'y=',y)
print("After changes with sign x="+'{:+.2f}'.format(x))
print("After changes with sign y="+'{:+.2f}'.format(y))
print('*'*40)

#31.n program to display a number with a comma separator.
num=3000000
print("original number",num)
print("After formatting"+"{:,}".format(num))
print('*'*40)

#32. Python program to format a number with a percentage.
num1=0.25
print("original value",num1)
print("After changing value="+"{:.2%}".format(num1))
print('*'*40)

#33.Count occurenaces of word in string
str6='The quick brown fox jumps over the lazy dog.'
print(str6.count('fox'))
print('*'*40)

#34.strip char in string
def stripstr(str,chars):
    return (''.join(c for c in str if c not in chars))

print(stripstr("The quick brown fox jumps over the lazy dog.","aeiou"))
print('*'*40)

#35.count reapeated character in string
str="The quick brown fox jumps over the lazy dog."
d2=dict()
for i in str:
    d2[i]=d2.get(i,0)+1
print(d2)
print('*'*40)

#36.count the index of each character in string
str='w3resource'
for i,j in enumerate(str):
    print(j,'present at index',i)

#37.Python program to check if a string contains all letters of the alphabet.
import string
alphabet=set(string.ascii_lowercase)
input_string = 'The quick brown fox jumps over the lazy dog'
print(set(input_string.lower()) >= alphabet)
input_string = 'The quick brown fox jumps over the lazy cat'
print(set(input_string.lower()) >= alphabet)
'''
'''
#38.convert string into list
str123='python programming'
list1=str123.split()
print(list1)

#38.lower the first n character in string
str='W3SOURCE'
print(str[:4].lower()+str[4:])

#39.convert dot to comma and comma to dot
amount = "32.054,23"
maketrans = amount.maketrans
amount = amount.translate(maketrans(',.', '.,'))
print(amount)

#40.count vowels in string
str='this is a python language'
vowels='aeiouAEIOU'
print(len([a for a in str if a in vowels]))
print([a for a in str if a in vowels])

#41
str='w,3,r,e,s,o,u,r,c,e'
print(str.rsplit(',',1))
'''
#42.Non repeated character in string
def NonReapted(str1):
    list1 = []
    ctr = dict()
    for c in str1:
        if c in ctr:
            ctr[c]+=1
        else:
            ctr[c]=1
            list1.append(c)
    for c in list1:
        if ctr[c] == 1:
            return c
    return None
print('first non repeated string is:')
print(NonReapted('aabcbcd'))

#43.first repeated character
str='kunalk'
for index,c in enumerate(str):
    if str[:index+1].count(c) > 1:
        print(c)
print('*'*40)

#44.Write a Python program to find the first repeated character of a given string where
# the index of first occurrence is smallest.
def first_repeated_char_smallest_distance(str1):
  temp = {}
  for ch in str1:
    if ch in temp:
      return ch
    else:
      temp[ch] = 0
  return 'None'
print(first_repeated_char_smallest_distance("abcabc"))
print(first_repeated_char_smallest_distance("abbcabc"))
print(first_repeated_char_smallest_distance("abcbabc"))
print(first_repeated_char_smallest_distance("abcxxy"))
print(first_repeated_char_smallest_distance("abc"))
print('*'*40)

#45.Write a Python program to find the second most repeated word in a given string.
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    counts_x = sorted(counts.items(), key=lambda kv: kv[1])
    #print(counts_x)
    return counts_x[-2]


print(word_count(
    "Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which executes expressions in annotations at their definition time, the compiler stores the annotation in a string form equivalent to the AST of the expression in question. If needed, annotations can be resolved at runtime using typing.get_type_hints(). In the common case where this is not required, the annotations are cheaper to store (since short strings are interned by the interpreter) and make startup time faster."))


#46.Write a Python program to remove spaces from a given string.
def removespace(str):
    str=str.replace(' ','')
    return str
print(removespace('a b c'))
print(removespace('k u n a l'))
print('*'*40)

#47.Write a Python program to capitalize first and last letters of each word of a given string.
def Capital(sr):
    str=result=sr.title()
    result=""
    for word in str.split():
        result +=word[:-1]+word[-1].upper()+ " "
    return result
print(Capital("python is great"))
print('*'*40)

#48.Remove the duplicate words in string
from collections import OrderedDict
def remove_duplicate(str1):
    return "".join(OrderedDict.fromkeys(str1))
print(remove_duplicate("python exercises practice solution"))
print(remove_duplicate("kunal hedgire"))
print('*'*40)

#50.count the digit from string
#s=input("Enter The String")
s='22sd55d'
c=0
for i in s:
    if i.isdigit():
        c +=int(i)
print('The count is:',c)
print('*'*40)

#51.Write a Python program to check if a string contains all letters of the alphabet.
import string
alpha=set(string.ascii_lowercase)
print(alpha)
inputstring = 'abcdefghijklmnopoqrstuvwxyz'
print(set(inputstring.lower()) >= alpha)
print('*'*40)


str='aaabba'
acount=0
bcount=1
atemp=0

for i in range(0,len(str)+1):
    if str[i] == str[i+1]:
        acount+=1
        atemp += 1
    elif str[i] != str[i+1]:
        bcount+=1
        #print('B', bcount)
        atemp=0
        continue

#print('A', acount)
    print('A', acount,'B', bcount,'A',atemp)


