'''
class ExceptionHnadler:

    def ExceptionHandle(self,num1,num2):
        result='Cant divide by zero'
        try:
            result=num1/num2
            print("Result is ", result)

        except:
            print(result)


a=ExceptionHnadler()
a.ExceptionHandle(10,0)
'''

def m1():
    print("Inside m1...4")
    result=10/0
    print("End m1..5")


def m2():
    print("Inside m2...3")
    m1()
    print("End m2..6")


def m3():
    print("Inside m3...2")
    try:
        m2()
    except:
        print("Exception occurs")
    print("End m3..7")
def m4():
    print("Inside m4...8")
    print("End m4..9")


if __name__ == '__main__':
    print("Inside main...1")
    m3()
    m4()
    print("End main..10")


def m1():

    try:
        print("in try")
        num=10/0
    except:
        print("in exception")
    else:
        print("num",num)
        print("In else")

m1()