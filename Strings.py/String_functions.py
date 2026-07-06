#functions - len,max,min,sorted

print(len('delhi'))#5
print(max('delhi'))#i
print(min('delhi'))#d
print(sorted('delhi'))#['d', 'e', 'h', 'i', 'l']

#capitalize, upper, lower, title, swapcase
print('delhi'.capitalize())#Delhi
print('delhi'.upper())#DELHI
print('DELHI'.lower())#delhi
print('delhi is capital of india'.title())#Delhi Is Capital Of India
print('delhi is capital of india'.swapcase())#DELHI IS CAPITAL OF INDIA

#count,find,index
print('delhi'.count('d'))#1 returns number of occurences
print('delhi'.find('d'))#0 returns index , otherwise -1
print('delhi'.index('d'))#0 returns index , otherwise error

#endswith,startswith
print('delhi'.endswith('i'))#true
print('delhi'.startswith('d'))#true

#format
name='delhi'
print('city is {}'.format(name))#city is delhi

#isalpha, isdigit, isspace,isidentifier,isalnum
print('delhi'.isalpha())#true
print('123'.isdigit())#true
print('   '.isspace())#true
print('delhi123'.isalnum())#true  
print('delhi'.isidentifier())#true

#split,join,replace
print('hi hello how are you'.split())#['hi', 'hello', 'how', 'are', 'you']
print('hi hello how are you'.split('h'))#['', 'i ', 'ello ', 'ow are you']
print(' '.join(['hi', 'hello', 'how', 'are', 'you']))#hi hello how are you
print('hi hello how are you'.replace('h','H'))#Hi Hello How are you

#strip,lstrip,rstrip
print('   hi hello how are you   '.strip())#hi hello how are you
print('   hi hello how are you   '.lstrip())#hi hello how are you
print('   hi hello how are you   '.rstrip())#   hi hello how are you

#remove,removeprefix,removesuffix
print('hi hello how are you'.removeprefix('hi '))#hello how are you
print('hi hello how are you'.removesuffix(' you'))#hi hello how are
