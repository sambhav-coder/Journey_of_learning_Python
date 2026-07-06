#write a program to check if list is sorted or not
N=int(input("enter size of list"))
L=[]
for i in range(N):
    item=int(input("enter a number"))
    L.append(item)

if L==sorted(L):
    print(True)
else:
    print(False)