#itemwise
L=[1,2,3,4,5]
for i in L:
    print(i)

#indexwise
L=[1,2,3,4,5]
for i in range(len(L)):
    print(L[i])

#zip()function return a zip object which is iterator of tuples
L1=[1,2,3,4]
L2=[11,12,13,14]
print(list(zip(L1,L2)))
print([[i,j] for i,j in zip(L1,L2)])
print([i+j for i,j in zip(L1,L2)])


#disadvantages of python list
# slow, risky usge, eats up more memory
