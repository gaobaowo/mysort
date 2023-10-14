class Solution:
    def p_Pow(self, x: float, n: int) -> float:
        tmp = x
        if x==0.0:
            return 0.0
        res = 1.0
        for i in range(31):
            if n % 2 == 1:
                res *= tmp
            n = n // 2
            tmp *= tmp
        return res
    def myPow(self, x: float, n: int) -> float:
        if n >= 0 :
            return self.p_Pow(x,n)
        else:
            n += 1
            n = abs(n)
            res=self.p_Pow(x,n)*x
            res=1.0/res
            return res
        

        
    
a=Solution()
print(a.myPow(2.0,-))