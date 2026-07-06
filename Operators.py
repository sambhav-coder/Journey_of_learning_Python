#operators are used to perform operations on variables and values
#arthmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, division, etc.
#addition +
#subtraction -
#multiplication *
#division / it returns the quotient of the division and keeps the decimal part
#floor division // it returns the quotient of the division and discards the decimal part
#modulus % 
#exponentiation **

a=12
b=5
c=a+b
print(c) #17
d=a-b
print(d) #7
e=a*b
print(e) #60
f=a/b
print(f) #2.4   
g=a//b
print(g) #2
h=a%b
print(h) #2
i=a**b
print(i) #248832

c=(12+5)**2/3-7*4%2
print(c) #96.33333

#assignment operators are used to assign values to variables
a=12
a+=5 #a=a+5
print(a) #17
#comparison operators are used to compare two values and return a boolean value(True or False)
a=12
b=5
print(a==b) #False  
print(a!=b) #True
print(a>b) #True
print(a<b) #False
#compound assignment operators are used to perform an operation and assign the result to the variable in a single step
#+=, -=, *=, /=, //=, %=, **=
a+=5 #a=a+5
print(a) #17
a-=5 #a=a-5
print(a) #12
a*=5 #a=a*5
print(a) #60
a/=5 #a=a/5
print(a) #12.0
a//=2 #a=a//2
print(a) #6.0
a%=2 #a=a%2
print(a) #0.0
print('A'>'a')
print(ord('A')) #65
print(ord('a')) #97

#logical operators are used to combine multiple conditions and return a boolean value(True or False)
a=12
b=5
print(a>10 and b<10) #True
print(a>10 or b<10) #True
print(not(a>10 and b<10)) #False
