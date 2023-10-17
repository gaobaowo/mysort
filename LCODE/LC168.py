x=701
result=""
while x!=0:
    result=chr((x % 26)+64)+result
    x//=26
    print(x%26)