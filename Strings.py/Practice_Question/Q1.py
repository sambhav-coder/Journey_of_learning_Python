#find length of given string without using len() function
m=input("Enter a string:")
count=0
for i in range(0,len(m)):
    count+=1
print("Length of given string is:",count)