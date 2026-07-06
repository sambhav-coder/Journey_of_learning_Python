temp=int(input("enter temperature:"))
if(temp<0):
    print("freezing cold")
elif(0<=temp<10):
    print("very cold")
elif(10<=temp<20):
    print("cold")
elif(20<=temp<30):
    print("pleasant")
elif(30<=temp<40):
    print("hot")
else:
    print("very hot")