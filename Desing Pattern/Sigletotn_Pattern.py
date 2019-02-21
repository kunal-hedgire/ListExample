'''
class OnlyOne:
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val
    instance = None
    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg
    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __str__(self):
        return "Value -- {}".format(self.instance.val)


a=OnlyOne("kunal")
print(id(a),'---',a)

b=OnlyOne("hedgire")
print(type(b),'---',b)
print(b)

print(a)
'''

class Singleton:
    __instance=None
    def __init__(self):
        if Singleton.__instance !=None:
            raise Exception('This class is singleton')
        else:
            Singleton.__instance = self

    @staticmethod
    def getInstance(self):
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance
s=Singleton()
print(s)
