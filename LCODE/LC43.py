class Solution:
    def toInt(self,dig: str)->int:
        x=0
        for ch in dig:
            x=x*10+ord(ch)-48
        return x    
    def toStr(self,Val)->str:
        x=Val
        str_result=""
        while x>0:
            str_result=str_result+chr(48+x%10)
            x=x//10
        str_result=str_result[::-1]    
        return str_result

    def multiply(self, num1: str, num2: str) -> str:
        val=self.toInt(num1)*self.toInt(num2)
        return self.toStr(val)
a=Solution()
print(a.multiply("1239","393"))




    