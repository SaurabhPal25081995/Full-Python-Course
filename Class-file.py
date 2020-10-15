# class Student:
#     gender = "Male"
#
#     def details(self):
#         return f"Name is {self.name} and age is {self.age}"
#
# obj = Student()
# obj2 = Student()
# print(obj,obj2)
#
# obj.name = "Saurbh"
# obj2.name = "Gagan"
# obj.age = 25
# print(obj.name,obj.age,obj2.name)
# print(Student.__dict__)
# print(obj.__dict__)
#
# print(obj.details())

#
# class Student:
#     def __int__(self, aname, aage, arole):
#         self.name = aname
#         self.age = aage
#         self.role = arole
#
#     def display(self):
#         return f"Name is {self.name}, age is {self.age} and role is {self.role}"
#
# obj = Student()
# obj.name = "Saurabh"
# print(obj.name)
#
# obj2 = Student("Gagan", 42, "VCS")
# print(obj2.name)
# #objGau = Student("Gagan", 12, "CBI")
# print(obj.name)

class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
         return cls(*string.split("-"))

harry = Employee("Harry", 255, "Instructor")
harry.change_leaves(44)
print(harry.no_of_leaves)

karan = Employee.from_dash("Karan-420-Kane")
print(karan.name)