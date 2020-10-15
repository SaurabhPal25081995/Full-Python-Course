class Player:
    public_var = "Saurabh public_var"
    _protected = "Pal _protected"
    __private ="Gagan __private"

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        return f"Name of Player is {self.name}, age is {self.age} and gender is {self.gender}"

class Employee(Player):
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    def display(self):
        return f"Name of Player is {self.name}, age is {self.age}"

emp = Employee("Ram",43,"Male")
print(emp.public_var)

play = Player("gsfs",32,"Male")
print(play._Player__private)  # Name Mangaling