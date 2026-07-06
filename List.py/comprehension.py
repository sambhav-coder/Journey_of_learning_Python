#list comprehension
#list comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an existing iterable (like a list, tuple, or string) and optionally filtering the items based on a condition.
L=[1,2,3,4,5]

#Example 1: Create a new list with the squares of each number in the original list
squares=[x**2 for x in L]
print(squares)  # Output: [1, 4, 9, 16, 25]

#ADD 1 TO 10 numbers to a list
L=[x for x in range(1,11)]
print(L)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#scalar multiplication
L=[1,2,3,4,5,7]
s=3
print([s*i for i in L])  # Output: [3, 6, 9, 12, 15, 21]    

#print all no divisible by 5 in range of 1 to 50
L=[i for i in range(1,51)if i%5==0]
print(L)  # Output: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

#find languages which start with letter 'P'
languages=['Python','Java','C++','Perl','Ruby']
L=[i for i in range(len(languages)) if languages[i][0]=='P']
print([languages[i] for i in L])  # Output: ['Python', 'Perl']  

#nested list comprehension
basket=['apple','guava','cherry','banana']
my_fruits=['apple','kiwi','banana','grapes']
common_fruits=[fruit for fruit in my_fruits if fruit in basket and (fruit.startswith('a')) ]
print(common_fruits)  # Output: ['apple']

#print a 3*3 matrix using list comprehension
matrix=[[i*j for i in range(1,4)] for j in range(1,4)]
print(matrix)  # Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

#cartesian products
L1=[1,2,3,4]
L2=[5,6,7,8]
cartesian_product=[i*j for i in L1 for j in L2]
print(cartesian_product)  # Output: [5, 6, 7, 8, 10, 12, 14, 16, 15, 18, 21, 24, 20, 24, 28, 32]    

