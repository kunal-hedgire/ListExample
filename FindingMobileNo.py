
import re
'''
file=open("C:\PythonProjects\ListExample\Ipfile.txt",'r').readlines()
for line in file:
    print(line)
    #s=re.findall(r"\+91\d{10}",line)
    s=re.findall(r"\D{jJ}ava",line)
    print(s)
'''
#match_num=re.search(r'^(\d{3}--\d{3}--\d{4})
#Email...->^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$
e='dasdasdasdasds kunalhedgire@gmail.com adsa.dakdlkajddkaskdaddiajdij kunalhegdire1993@gmail.com'

print(re.findall(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",e,re.I))


