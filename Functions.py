#Functions in python is a block of code that can be reuse by calling function name
#built in functions like print(),input(),len()
#function created by us are called user defined functions
#def keyword use krna padega

l=int(input("enter length:"))
b=int(input("enter breadth"))

def area_rect(l,b): #defining function
    area=l*b
    return area

print(area_rect(l,b)) # calling function 
