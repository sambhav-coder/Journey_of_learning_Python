#1/1! + 2/2! + 3/3! + ...
n=int(input("Enter the value of n: "))
sum=0
fac=1
for i in range(1,n+1):
    fac=fac*i
    sum=sum+(i/fac)
print(sum)

