# Write a program to replace an item with a different item if found in the list 
L = [1,2,3,4,5,3]
# replace 3 with 300
L=[300 if i==3 else i for i in L]
print(L)