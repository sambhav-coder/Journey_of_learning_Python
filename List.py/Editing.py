#edit
L=[1,2,3]
L[0]=0
print(L)  # Output: [0, 2, 3]

L[0:2]=[6,5]
print(L)  # Output: [6, 5, 3]   

#delete
L=[1,2,3]
del L[0]
print(L)  # Output: [2, 3]
del L[0:2]
print(L)  # Output: []

#remove
L=[1,2,3]
L.remove(2)
print(L)  # Output: [1, 3]

#pop
L=[1,2,3]
L.pop()
print(L)  # Output: [1, 2]
L.pop(0)
print(L)  # Output: [2]

#clear
L=[1,2,3]
L.clear()
print(L)  # Output: []