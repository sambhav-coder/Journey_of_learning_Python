#loops in python are used to execute a block of code repeatedly until a certain condition is met. There are two main types of loops in Python: for loops and while loops.
#for loops are used to iterate over a sequence (such as a list, tuple, or string) and execute a block of code for each item in the sequence. The syntax for a for loop is as follows:
#for item in sequence:
#    # code to be executed for each item
#while loops are used to execute a block of code repeatedly as long as a certain condition is true. The syntax for a while loop is as follows:
#while condition:
#    # code to be executed while the condition is true      

#range() function is used to generate a sequence of numbers. It can take one, two, or three arguments. The syntax for the range() function is as follows:
#range(stop) - generates a sequence of numbers from 0 to stop-1
#range(start, stop) - generates a sequence of numbers from start to stop-1
#range(start, stop, step) - generates a sequence of numbers from start to stop-
#example of for loop using range() function:
for i in range(5):
    print(i)
for i in range(1, 10):
    print(i)
for i in range(1, 10, 2):
    print(i)

#example of while loop:
i = 0
while i < 5:
    print(i)
    i += 1

#example 2 of while loop:
i = 1
while i <= 10:
    print(i)
    i += 1

#example of nested loops:
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# reverse counting using for loop:
for i in range(16, 0, -1):
    print(i)

for i in range(-3,-16,-1):
    print(i)

#string ex for loop
a="python"
for i in range(2,len(a),2):
    print(a[i])
for i in a:
    print(i)

# example using break statement
for i in range(1,11):
    if(i==5):
        break
    print(i)

# example using continue statement
for i in range(1,11):
    if(i==5):
        continue
    print(i)

# use of else statement with for loop
for i in range(1,6):
    print(i)
else:
    print("Loop completed successfully")

#example 2 use of else statement with for loop
for i in range(1,6):
    if(i==3):
        break
    print(i)
else:
    print("Loop completed successfully")

# example of nested loops with break statement
for i in range(1, 4):
    for j in range(1, 4):
        if(i==2 and j==2):
            break
        print(i, j)
else:
    print("Inner loop completed successfully")  

#use of elif statement with for loop
for i in range(1, 6):
    if(i==3):
        print("Three")
    elif(i==5):
        print("Five")
    else:
        print(i)

