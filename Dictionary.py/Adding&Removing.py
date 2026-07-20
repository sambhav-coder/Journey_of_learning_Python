#Adding key-value pair
dict={'name':'jack','age':26}
dict['gender']='male'
dict['birth place']='delhi'
print(dict)

#removing key-pair
#pop,pop item,del,clear

#pop
dict.pop('gender')
print(dict)

#pop item
dict.popitem()
print(dict)

#del
del dict['name']
print(dict)

#clear
dict.clear()
print(dict)