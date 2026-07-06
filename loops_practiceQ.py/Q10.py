#reverse a string without using in build functions
s=input("enter a string :")
b=""
for i in range(len(s)-1,-1,-1):
    b=b+s[i]
print(b)
