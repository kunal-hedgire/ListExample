'''
class Vehicle:

    @classmethod
    def getInstance(cls,ty,param1,param2):
        if ty == 'A':
            return Audi(param1,param2)
        elif ty == 'B':
            return BMW(param1,param2)
        else:
            print('no criteria found')
            return None


class Audi:

    def __init__(self,id,nm):
        self.carName = nm
        self.carId = id

    def __str__(self):
        return 'AudiId : {}, Name : {}'.format(self.carId,self.carName)


class BMW:

    def __init__(self,id,nm):
        self.Name = nm
        self.Id = id

    def __str__(self):
        return 'ID :{} , Name :{}'.format(self.Id,self.Name)


b = Vehicle.getInstance('B',1,'BWMSeris')
a = Vehicle.getInstance('A',1,'BWMSeris')

print(type(b))# bmw
print(type(a))# bmw
'''
#MyExample

class vehicle:
    @classmethod
    def getinstance(cls,ty,param1,param2):
        if ty =='A':
            return Audi(param1,param2)
        elif ty =='B':
            return BMW(param1,param2)
        else:
            print('No criteria found')
            return None

class Audi:

    def __init__(self,id,nm):
        self.carid=id
        self.carname=nm

    def __str__(self):
        return 'AudiName :{},AudiId :{}'.format(self.carname,self.carid)

class BMW:

    def __init__(self,id,nm):
        self.carid=id
        self.carname=nm

    def __str__(self):
        return 'BMWName :{},BMWId :{}'.format(self.carname,self.carid)


a=vehicle.getinstance('B','1','AudiSeries')
b=vehicle.getinstance('A','1','BMWSeries')

print(type(a))
print(type(b))



























