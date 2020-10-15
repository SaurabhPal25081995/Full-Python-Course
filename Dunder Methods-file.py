class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def __add__(self, other):
        return self.salary + other.salary

emp1 = Employee("Saurabh",300)
emp2 = Employee("Gagan",300)
print(emp1+emp2)