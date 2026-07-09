#len,sum,min,max,sorted
s = {3,1,4,5,2,7}
print(len(s))
print(sum(s))
print(min(s))
print(max(s))
print(sorted(s,reverse=True))

# union/update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

# s1 | s2
print(s1.union(s2))

s1.update(s2)
print(s1)
print(s2)

# intersection/intersection_update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

print(s1.intersection(s2))

s1.intersection_update(s2)
print(s1)
print(s2)

# difference/difference_update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

print(s1.difference(s2))

s1.difference_update(s2)
print(s1)
print(s2)

# symmetric_difference/symmetric_difference_update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

print(s1.symmetric_difference(s2))

s1.symmetric_difference_update(s2)
print(s1)
print(s2)

# isdisjoint/issubset/issuperset
s1 = {1,2,3,4}
s2 = {7,8,5,6}

print(s1.isdisjoint(s2))

s1 = {1,2,3,4,5}
s2 = {3,4,5}

print(s1.issuperset(s2))

# copy
s1 = {1,2,3}
s2 = s1.copy()

print(s1)
print(s2)

#frozen set-- frozen set is an immutable version of python set means we cant add del or remove items in set

#create a frozen set
fs=frozenset([1,2,3])
print(fs)
# what works and what does not
# works -> all read functions
# does't work -> write operations

# When to use
# 2D sets
fs = frozenset([1,2,frozenset([3,4])])
print(fs)