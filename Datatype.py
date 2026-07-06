a=12
print(type(a))
b=23.5
print(type(b))
c=1234567890123456
print(type(c))
d=12/3
print(type(d))
e=34j
print(type(e))
name="ajay"
print(type(name))
name1='ajay'
print(type(name1))
f=True
print(type(f))

#strings
a="hello"
print(a[0]) #h
print(a[1]) #e
#print(a[5]) #out of range error because index 5 is not present in the string
print(a[-1]) #o
print(a[-2]) #l
print(a[-5]) #h
#print(a[-6]) #out of range error because index -6 is not present in the string
print(a[0:4:2])#hl
print(a[0:4])#hell
print(a[-1:-5:-2])#ol

name="ajay gupta"
print(name[0:5])#ajay
print(name[5:11])# gupta    
print(name[0:11:2])#aa ut
print(name[0::])#ajay gupta

#type conversion
a=12
print(type(a))
a=str(a)
print(type(a))

a=12
print(bool(a)) #True
a=0
print(bool(a)) #False
#false values are 0, 0.0, "", [], (), {}, None
#true values are all other values except false values


