#program to convert 2D list into 1d list
L=[[1,2],[3,4]]
L1=[]
for i in range(0,len(L)):
    L1.extend(L[i])
print(L1)