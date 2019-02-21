#import openpyxl
import re

print(re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", open("C:\PythonProjects\ListExample\Ipfile.txt",'r').read()))

