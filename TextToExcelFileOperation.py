#import xlrd
import xlwt as write

class ExcelOpeartion:
    FilePath =r"C:\PythonProjects\ListExample\user.xls"
    list1=[]
    def getData(self):
        file =open("C:\PythonProjects\ListExample\TextFile.txt")
        #msg=file.readlines()
        #print(msg)

        for items in file.readlines():
            #print(file.readlines())
            ExcelOpeartion.list1.append(items.strip())

    def Data(self):
        workBook=write.Workbook()
        sheet=workBook.add_sheet('Info')
        count=0
        cols=[]
        for line in ExcelOpeartion.list1:
            #print(line)
            for words in line.split(','):
                print(words)
                cols.append(words)

        for num in range(ExcelOpeartion.list1.__len__()):
            row = sheet.row(num)
            for item in range(5):
                row.write(item, cols.__getitem__(count))
                count += 1

        workBook.save(ExcelOpeartion.FilePath)

if __name__ == '__main__':
    m=ExcelOpeartion()
    m.getData()
    m.Data()
    #print(ExcelOpeartion.list1)





