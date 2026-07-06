str1="P@#yn26at^&i5ve"
Chars=0
Digits=0
Symbols=0
for i in range(0,len(str1)):
    if('0'<=str1[i]<='9'):
        Digits+=1
    elif('a'<=str1[i]<='z' or 'A'<=str1[i]<='Z'):
        Chars+=1
    else:
        Symbols+=1

print("Chars"+"=",Chars)
print("Digits"+"=",Digits)
print("Symbols"+"=",Symbols)