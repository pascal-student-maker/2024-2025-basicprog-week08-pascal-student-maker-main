class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"{self.make} {self.model}")
class Person:
    #init methode or constructor
    def __init__(self,name):    
        self.name = name   
        def say_hi(self):
            print('Hello my name is ',self.name)
p = Person('nikhil')
p.say_hi()         
        