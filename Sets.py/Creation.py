#empty
s=set()
print(type(s))

#1D and 2D
s1={1,2,3}
print(s1)

#s2={1,2,3,{4,5}} #nested sets are not allowed
#print(s2)

#homo and hetro
s2={1,'hello',4.5,True} #hetro contain diff data types #True is treated as 1, so no duplicate is allow
# on printing input order is not same as output order because sets folllow unordered
print(s2)

s3={1,2,3,4} #homo contain same type of data types
print(s3)

#using type conversion
s4=set([1,2,3,4])
print(s4)

#duplicates not allowed
s5={1,2,2,3,3,3,4,4}
print(s5)

#set can't have mutable items
#s6={1,2,[3,4]} # throws error as it contains a list which is mutable
#print(s6)