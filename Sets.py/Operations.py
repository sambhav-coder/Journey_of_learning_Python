#Union(|)
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1 | s2) # merge two set remove duplicate

#Intersection(&)-- s1&s2 common items
print(s1&s2)

#difference(-)-- s1-s2 jo element sirf s1 main ho
print(s1-s2)

#symmetric diff(^)-- common chod kr baaki sab print
print(s1^s2)

#membership test
print(1 in s1)
print(6 not in s2)

#iteration
for i in s1:
    print(i)

