age=int(input("enter your age:"))
if(0<age<18):
    print("u are minor")
        
elif(18<=age<60):
    print("u are adult")
        
elif(age>=60):
    print("u are senior citizen")
else:
    print("invalid age")        