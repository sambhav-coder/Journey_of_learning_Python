#append
L=[1,2,3]
L.append(4)
print(L)  # Output: [1, 2, 3, 4]
L.append([5,6])
print(L)  # Output: [1, 2, 3, 4, [5, 6]]

#extend
L=[1,2,3]
L.extend([4,5])
print(L)  # Output: [1, 2, 3, 4, 5]
L.extend((6,7))
print(L)  # Output: [1, 2, 3, 4, 5, 6, 7]

#insert
L=[1,2,3]
L.insert(1, 1.5)
print(L)  # Output: [1, 1.5, 2, 3]
L.insert(0, 0)
print(L)  # Output: [0, 1, 1.5, 2, 3]
