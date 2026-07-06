#check a no is perfect sq or not
import math
n=int(input("enter a no:"))
m=int(math.sqrt(n))
if(m*m==n):
    print(True)
else:
    print(False)