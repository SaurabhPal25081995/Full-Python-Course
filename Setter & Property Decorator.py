class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}{lname}@gmail.com"

    # def explain(self):
    #     return f"Employe is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email does not exist"
        return f"{self.fname}{self.lname}@yahoo.com"

    @email.setter
    def email(self,string):
        var = string.split("@")[0]
        self.fname = var.split(".")[0]
        self.lname = var.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

pal = Employee("Saurabh","Pal")
print(pal.email)

pal.fname = "Gagan"
print("Changed email is -",pal.email)
print("Changed fname is -",pal.fname)

pal.email = "new.email@gmail.com"
print("Changed mail by setter -",pal.email)
print(pal.fname)
print(pal.lname)

del pal.email
print(pal.email)