#len
L=[1,2,3]
print(len(L))  # Output: 3  

#min and max
L=[1,2,3]
print(min(L))  # Output: 1
print(max(L))  # Output: 3  

#sort #permanent operation
L=[3,1,2]
L.sort()
print(L)  # Output: [1, 2, 3]

#sorted temporary operation
L=[3,1,2]
S=sorted(L)
print(S)  # Output: [1, 2, 3]

#count
L=[1,2,3,2]
print(L.count(2))  # Output: 2

#index
L=[1,2,3]
print(L.index(2))  # Output: 1

#reverse
L=[1,2,3]
L.reverse()
print(L)  # Output: [3, 2, 1]

#copy creates a copy with diff memory location 
L=[1,2,3]
L_copy=L.copy()
print(L_copy)  # Output: [1, 2, 3]


