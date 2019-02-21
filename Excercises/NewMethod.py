'''
class NEW:
    def __new__(cls, *args, **kwargs):
        print("Creating instance")
        instance=super(NEW,cls).__new__(cls,*args,**kwargs)
        return instance
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def bar(self):
        pass

n=NEW(' ',' ')
'''
import datetime

today=datetime.datetime.now()
print(str(today))
print(repr(today))






















