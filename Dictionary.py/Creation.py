#empty dictionary
d={}
#1D dictionary
d1={'name':'samar','gender':'male'}
#with mixed keys
d2={(1,2,3):1,'hello':'world'}

#2D dictionary
s={'name':'samar','college':'IPU','sem':4,'subjects':{'dsa':50,'oops':67,'cn':85,'pslp':82}}

#using sequence and dict function
d3=dict([(1,1),(2,2),(3,3)])
print(d3)

#duplicate keys
d5={'name':'raj','name':'shyam'}
print(d5)# in case of duplicate key it will print last item

#mutable item as key not allowed
#ex- d6={'name':'raj',[1,2,3]:2} 