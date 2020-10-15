class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


class Programmer(Employee): # Inheritance
    no_of_leaves = 88

    def __init__(self, aname, asalary, arole, alang):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.lang = alang

    def printprog(self):
        return f"Printprog, My name is {self.name}. Salary is {self.salary}, role is {self.role} and langauges is {self.lang}"

harry = Employee("Harry", 255, "Instructor")
print(harry.name, harry.salary, harry.role)

pal = Programmer("Pal",444,"Coder",["python","c++","c","java"])
print(pal.printprog())
print(harry.no_of_leaves)

