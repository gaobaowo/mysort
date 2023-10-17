class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split()
        a=a[::-1]
        result=a[0]
        for i in range(1,len(a)):
            result+=" "+a[i]
        
        return result
x=Solution()
print(x.reverseWords("the sky is good blue"))