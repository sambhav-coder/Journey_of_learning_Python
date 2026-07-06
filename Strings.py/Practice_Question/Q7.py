#to convert a string to title case without using title() function
s=input("Enter a string: ")
words=s.split()
for i in range(len(words)):
    words[i]=words[i].capitalize()
s=" ".join(words)
print(s)