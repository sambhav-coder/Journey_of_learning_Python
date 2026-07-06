# write a program to remove duplicate item from List
L=[1,2,1,2,3,4,5,3,4]
L1=[]
for i in L:
    if i not in L1:
        L1.append(i)
print(L1)
