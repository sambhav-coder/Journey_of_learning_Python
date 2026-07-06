#check palindrome of string
s=input("enter a string :")
palindrome=True
for i in range(0,len(s)):
    if(s[i]!=s[len(s)-1-i]):
        palindrome=False
        break;

if palindrome:
    print(True)
else:
    print(False)