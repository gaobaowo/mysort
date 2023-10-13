class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #str = "adkfdsjkvdskjshvdsdj324213ncdsn4rDDDDASaa123"
        n_row = numRows
        strs=[]
        dat=[]
        str=s
        result=""
        if n_row==1:
            return str
        if n_row ==2:
            for i in range(len(str)) :
                if i%2==0:
                    result +=str[i]
            for i in range(len(str)):
                if i%2==1:
                    result +=str[i]
            return result
        l = len(str)
        m = l // (2 * n_row - 2)
        k = l % (2 * n_row - 2)

        for i in range(m):
            strs.append(str[i * (2 * n_row - 2) : (i+1)*(2 * n_row-2)])
        for s in strs:
            ss = s[:n_row]
            sss = '\n'+s[n_row:]+'\n'
            sss = sss[::-1]
            dat.append(ss)
            dat.append(sss)

        if k >= 0:
            if k>n_row:
                ss = str[-k:-k+n_row]
                sss = str[-k+n_row:]
                rl = len(sss)
                sss = "\n"+sss+"\n"*(n_row-rl-2)
                sss = sss[::-1]
                dat.append(ss)
                dat.append(sss)
            else:
                ss=str[-k:]+"\n"*(n_row-k)
                dat.append(ss)
        result=""
        print(dat)
        for i in range(n_row):
            for j in range(len(dat)):
                if dat[j][i]!="\n":
                    result += dat[j][i]
        return result

a=Solution()
lstr="abcdssss"
print(a.convert(lstr,5))
            
            