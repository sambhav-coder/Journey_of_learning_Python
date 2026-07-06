#count the frequency of a particular character in a provided string
s=input("enter a string:")
char=input("enter a char to find:")
count=0
for i in range(0,len(s)):
    if s[i]==char:
         count+=1
print("the frequency of",char,"in this string is",count)

         