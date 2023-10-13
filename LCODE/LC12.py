rom=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
values=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
class Solution:
    def intToRoman(self, num: int) -> str:
        result=''
        num_int=num
        for i in range(13):
            while (num_int-values[i]) >= 0:
                result+=rom[i]
                num_int-=values[i]
        return result
    
a=Solution()
print(a.intToRoman(1994))
