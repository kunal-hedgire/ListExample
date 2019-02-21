from openpyxl import *
import pymysql

conn= pymysql.connect(host='localhost',port=3306,user='root',passwd='tiger',db='basic')



print('press 1 for insert data into TEXT FILE','\npress 2 for insert data into Database','\npress 3 for insert data into EXCEL FILE','\npress 4 for print data on Console' )

choice=input('\nEnter your choice:')


if int(choice) == 1:
    with open('C:\PythonProjects\ListExample\Ipfile.txt','a') as file:
        print('Your writing in TEXT FILE')
        a=input('Enter The Name:')
        b=input('Enter The Address:')
        c=input('Enter the Course:')
        file.writelines(a+'\t')
        file.writelines(b+'\t ')
        file.writelines(c+'\n')
        print('data is inserted successfully')
        file.close()

elif int(choice) == 2:
    print('Your writing in DATABASE')
    name = input('Enter The Name:')
    age = input('Enter The Age:')
    course = input('Enter the Course:')
    cur=conn.cursor()
    query = "insert into user (name,age,course) values('"+name+"','"+age+"','"+course+"')"
    print(' data is inserted successfully')
    cur.execute(query)

elif int(choice)==3:
    print('Your wirting in XML FILE')

    filepath = "C:\PythonProjects\ListExample\Data.xls"
    wb = load_workbook(filepath)
    sheet = wb.active
    name = input('Enter The Name:')
    adrress = input('Enter The Address:')
    course = input('Enter the Course:')
    sheet['A2'] = name
    sheet['B2'] = adrress
    sheet['C2'] = course
    print('success')


elif int(choice)==4:
    pass







