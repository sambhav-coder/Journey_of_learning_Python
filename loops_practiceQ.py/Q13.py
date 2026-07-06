#using while loop seprate each digit of a no and print it on new line
n=int(input("enter a no:"))
while(n>0):
    rem=n%10
    print(rem)
    n=n//10