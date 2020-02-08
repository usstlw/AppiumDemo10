class A:
    t=1
    def m_a(self):
        a=1
        print("A.m_a")
        print(a)

class B:
    def m_b(self):
        print("B.m_b")

a1=A()
a2=A()

A.t=5
print(a1.t) #5
print(a2.t) #5

a1.t=2
print(a1.t)  #2
print(a2.t)  #5

a2.t=3
print(a1.t)  #2
print(A.t)  #5

A.t=5
print(a1.t)
print(a2.t)
print(A.t)