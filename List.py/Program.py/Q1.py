#create 2 list from given list where
# 1st list will contain all odd numbers from original list
# 2nd will contain all even members
L=[1,2,3,4,5,6]
L1=[i for i in range(len(L)) if i%2!=0]
print(L1)
L2=[i for i in range(len(L)) if i%2==0]
print(L2)

