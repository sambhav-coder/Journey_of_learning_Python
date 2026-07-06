#check palindrome of a no eg 121 hai toh rev 121 original ke barabar hai toh palindrome hai otherwise not
n=int(input("enter a no: "))
rev=0
copy=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10

if copy==rev:
    print("palindrome no")
else:
    print("not a palindrome no")