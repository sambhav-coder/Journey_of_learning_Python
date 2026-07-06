#extract username from given email address
email=input("enter your email address:")
for i in range(0,len(email)):
    if email[i]=='@':
        break
print(email[0:i])