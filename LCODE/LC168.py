class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        x = columnNumber
        while x != 0:
            r = x % 26
            x //= 26
            if r ==0:
                r = 26
                x-=1
            result = chr(r + 64) + result
            
            # print(f'r={r}   x={x}')
        return result
a=Solution()
print(a.convertToTitle(1))