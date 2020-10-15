class A:
    def met(self):
        print("Method in clas A")
class B(A):
    def met(self):
        print("Method in clas B")
class C(A):
    def met(self):
        print("Method in clas C")
class D(B,C):
    def met(self):
        print("Method in clas D")
        print("Method in clas D")
        print("Method in clas D")

a = A()
b = B()
c = C()
d = D()

d.met()