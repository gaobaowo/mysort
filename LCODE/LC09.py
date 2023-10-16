class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str=[]
        r=0
        while x > 0:
            r = x % 10
            str.append(r)
            x //=10
        return str == str[::-1]

a=Solution()
print(a.isPalindrome(12231))