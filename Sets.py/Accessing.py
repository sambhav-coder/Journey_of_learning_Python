s1={1,2,3,4}
# we cant use indexing,slicing as set is unordered

#editing -- we cant edit items in set

#adding items-- yes we can add items in set
s1.add(5)
print(s1)

#update-- we can add multiple items
s1.update([5,6,7])
print(s1)

#deleting items
#del
s={1,2,3,4,5}
del s
#print(s)

#discard
s2={2,3,5}
s2.discard(5) #if i put no which is outside of set, it simply dont change set and dont throw error
print(s2)

#remove
s2.remove(3)# if i put no which is outside of set,it throw error
print(s2)

#pop
s3={1,2,3,6,7}
s3.pop()# it delete random item
print(s3)

#clear
s3.clear()# it cleares the set and make empty set
print(s3)