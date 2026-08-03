class A:
    def method(self):
        print("A")
class B(A):
    def method(self):
        print("B")
        super().method()
class C(A):
    def method(self):
        print("C")
        super().method()
class D(B, C):
    def method(self):
        print("D")
        super().method()
d=D()
d.method()
