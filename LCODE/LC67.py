class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)>=len(b):
            x=a[::-1]
            y=b[::-1]
        else:
            x=b[::-1]
            y=a[::-1]
        sum=""
        c="0"
        for i in range(abs(len(a)-len(b))):
            y+="0"
        l=len(y)
        print(f"y={y}")
        for i in range(l):
            z=[x[i],y[i],c]

            if z==["0","0","0"]:
                c="0"
                sum+="0"
            elif z==["0","0","1"]:
                c="0"
                sum+="1"
            elif z==["0","1","0"]:
                c="0"
                sum+="1"
            elif z==["0","1","1"]:
                c="1"
                sum+="0"
            elif z==["1","0","0"]:
                c="0"
                sum+="1"
            elif z==["1","0","1"]:
                c="1"
                sum+="0"
            elif z==["1","1","0"]:
                c="1"
                sum+="0"
            elif z==["1","1","1"]:
                c="1"
                sum+="1"
            print(f"z={z}sum={sum}")
        if c=="1":
            sum+="1"
        sum=sum[::-1]
        return sum
adder=Solution()
str1="11"
str2="1"
print(f"str1={str1}")
print(f"str2={str2}")
print(adder.addBinary(str1,str2))