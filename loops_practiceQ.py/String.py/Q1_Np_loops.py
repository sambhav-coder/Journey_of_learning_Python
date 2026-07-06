"""Pattern 1
***
****
*** """

for i in range(1,4):
    for j in range(1,5):
        if (i==1  or i==3)and j==4:
            break
        print("*",end="")
    print()
