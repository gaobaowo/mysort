ch2int={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
class Solution:
    def romanToInt(self, s: str) -> int:
        str1=s[::-1]
        print(str1)
        result=ch2int[str1[0]]
        L=len(str1)
        print(range(1,L-2))
        for i in range(0,L-1):
            if ch2int[str1[i]] > ch2int[str1[i+1]]:
                result-=ch2int[str1[i+1]]
            else:
                result+=ch2int[str1[i+1]]
        return result
    
x=Solution()
print(x.romanToInt("MCMXCIV"))