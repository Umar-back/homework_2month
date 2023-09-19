from homework4 import First, Second, Third, Fourth

class Fifth(First, Second, Third, Fourth):
    def  __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age

    def get_age(self):
        return self.__age

    def age(self):
        return self.__age

    def age(self, age2):
        self.age2 = age2