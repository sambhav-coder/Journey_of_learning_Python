#len/sorted
d5={'name':'raj','age':32,'gender':'male'}
print(len(d5))
print(sorted(d5))# a list of keys in accesending order
print(sorted(d5,reverse=True))
print(max(d5))

s={'name':'samar','college':'IPU','sem':4,'subjects':{'dsa':50,'oops':67,'cn':85,'pslp':82}}
print(len(s))
print(sorted(s))
print(max(s))

#items/keys/values
print(d5.items())
print(d5.keys())
print(d5.values())

#update
d1={1:1,2:2,3:3,4:4}
d2={4:7,6:8}
d1.update(d2)
print(d1)

#dictionary comprehension
#print 1st 10 number and their squares
d={i:i**2 for i in range(1,11)}
print(d)

#using existing dict
dis={'delhi':1000,'mumbai':2000,'banglore':3000}
dis={i:j*0.62 for (i,j) in dis.items()}
print(dis)

#using zip
days=['sun','mon','tue','wed','thu','fri','sat','sun']
temp_C=[30,32,31,33,29,30,26]
dict={i:j for (i,j)in zip(days,temp_C)}
print(dict)

#using if condition
product={'phone':10,'laptop':0,'charger':32,'tablet':0}
product={i:j for(i,j)in product.items() if j>0}
print(product)

#nested comprehension
# print tables of number 2 to 4
table={i:{j:i*j for j in range(1,11)}for i in range(2,5)}
print(table)
