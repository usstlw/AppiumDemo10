def fun2(a,b,c):
    print(a+b+c)

# a=[1,2,3]
#
# fun2(1,2,3)
# fun2(a[0],a[1],a[2])
# fun2(*a)


# print(*a)

# b = {"a":1,"b":2}
# print(**b)


def fun3(a=6,b=2):
    print(a*b)



b={"a":3,"b":2 }
fun3(a=3,b=2)

# fun3(**b)

a=[1,2,3]
print(dir(a))


d={'a':2,'b':'bbb'}
print(d.keys())
print(d.values())
print(d.get('a'))
print(d['a'])