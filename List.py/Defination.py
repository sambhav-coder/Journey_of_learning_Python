#lists are mutable, ordered collections of items. They can contain elements of different data types, including other lists. Lists are defined using square brackets [] and can be modified after their creation.    
L=[1, 2, 3, 4, 5]
print(L)
L=[1,'hello', 3.14, [1, 2, 3]]
print(L)

#Array vs List: In Python, lists are more versatile than arrays. Lists can hold elements of different data types, while arrays (from the array module) are more efficient for large collections of homogeneous data types. Lists also provide a wide range of built-in methods for manipulation.
#fixed vs dynamic: Lists are dynamic in size, meaning they can grow or shrink as needed. Arrays, on the other hand, have a fixed size once created.
#speed of execution: Arrays can be faster for certain operations, especially when dealing with large datasets of the same type, due to their fixed size and lower-level implementation. Lists may have some overhead due to their dynamic nature and ability to hold mixed data types.
#memory usage: Arrays typically use less memory than lists for large collections of homogeneous data types, as they are more compact and have less overhead. Lists may consume more memory due to their dynamic nature and ability to store mixed data types.

#how list are stored in memory: 
# Lists are stored as arrays of pointers to the actual objects in memory. Each element in a list is a reference to an object, which allows for dynamic resizing and the ability to hold elements of different types. The list itself maintains a contiguous block of memory for these references, and when the list grows beyond its current capacity, it allocates a new larger block of memory and copies the references over.

#dynamic array in python:
# In Python, lists are implemented as dynamic arrays. When a list is created, it allocates a certain amount of memory to hold its elements. If the list exceeds this allocated space, Python automatically resizes the list by allocating a new larger block of memory and copying the existing elements to this new block. This resizing operation is typically done in a way that minimizes the number of times it needs
 #   to occur, often by increasing the size of the list by a factor (e.g., doubling its size) when it runs out of space. This allows lists to efficiently handle dynamic growth while maintaining performance.
L=[1,2,3]
L1=[1,3,2] #order matters in list comparison
print(L==L1)

