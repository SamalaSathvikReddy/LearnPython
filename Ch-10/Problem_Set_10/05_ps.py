'''
Write a Class 'Train' which has methods to book a ticket, get status (no of seats)
and get fare information of train running under Indian Railways.
'''
from random import randint

class Train:
    def __init__(self,trainNo,fro,to):
        self.trainNo = trainNo
        self.fro = fro
        self.to = to

    def book(self):
        print(f'Your seat is book in train no {self.trainNo} from {self.fro} to {self.to}')

    def getStatus(self):
        print(f'Train no: {self.trainNo} going from {self.fro} to {self.to} is on the way.')

    def Fare(self):
        print(f'The fare for Trainno:{self.trainNo} going from {self.fro} to {self.to} is {randint(300,3000)}')


t = Train(12654,'Hyderabad','Banglore')

t.book()
t.Fare()
t.getStatus()
