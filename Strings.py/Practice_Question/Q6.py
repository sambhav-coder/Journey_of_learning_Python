#count no of words without using split function
s=input("Enter a string: ")
temp=''
l=[]
for i in s:
    if i!=" ":
        temp=temp+i
    else:
        l.append(temp)
        temp=''
l.append(temp)
print(l)