#empty tuple
t1=()
print(t1)

#create a tuple with a single item
t2=(2)
print(type(2)) # this will return class int that means this is not right way to define tuple

t3=(3,)
print(t3)
print(type(t3))

#homogenous tuple--- A tuple which contains element of same type
t4=(1,2,3,4,5)
print(t4)

#heterogeneous tuple--- A tuple which contains element of diff type
t5=(1,2.5,True,'hello')
print(t5)

#nested tuple
t6=(1,2,3,(4,5))
print(t6)

#using type conversion
t7=tuple('hello')
print(t7)

#user input
t=tuple(map(int,input("enter number :").split()))
print(t)

s=tuple(map(str,input("enter fruits:").split()))
print(s)