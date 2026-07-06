#conditional statements are used to perform different actions based on different conditions
a=12
b=5
if(a>b):
    print("a is greater than b :",a)
else:
    print("b is greater than a :",b)

#if elif else statement is used to perform multiple conditions
# simple programm to calculate scorecard
# 90-100 A+
#80-89 A
#70-79 B
#60-69 C
#0-59 Fail

m=int(input("enter marks:"))
while(m<0 or m>100):
    print("invalid marks")
    m=int(input("enter marks:"))
if(m>=90 and m<=100):
    print("A+")
elif(m>=80 and m<=89):
    print("A")
elif(m>=70 and m<=79):
    print("B")
elif(m>=60 and m<=69):
    print("C")
else:
    print("Fail")




