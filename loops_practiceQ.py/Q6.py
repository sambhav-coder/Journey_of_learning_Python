#sum of all even and odd numbers in a range seprately
n=int(input("enter a no :"))
sumO=0
sumE=0
for i in range(1,n+1):
    if(i%2==0):
        sumE=sumE+i
    else:
        sumO=sumO+i

print(sumE)
print(sumO)