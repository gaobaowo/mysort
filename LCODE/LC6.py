class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #str = "adkfdsjkvdskjshvdsdj324213ncdsn4rDDDDASaa123"
        n_row = numRows
        strs=[]
        dat=[]
        str=s
        if n_row==1:
            return str
        l = len(str)
        m = l // (2 * n_row - 2)
        k = l % (2 * n_row - 2)

        for i in range(m):
            strs.append(str[i * (2 * n_row - 2) : (i+1)*(2 * n_row-2)])
        for s in strs:
            ss = s[:n_row]
            sss = '*'+s[n_row:]+'*'
            sss = sss[::-1]
            dat.append(ss)
            dat.append(sss)

        if k >= 0:
            if k>n_row:
                ss = str[-k:-k+n_row]
                sss = str[-k+n_row:]
                rl = len(sss)
                sss = "*"+sss+"*"*(n_row-rl-2)
                sss = sss[::-1]
                dat.append(ss)
                dat.append(sss)
            else:
                ss=str[-k:]+"&"*(n_row-k)
                dat.append(ss)
        result=""
        print(dat)
        for i in range(n_row):
            for j in range(len(dat)):
                if i==0:
                    if j % 2==0 :
                        result += dat[j][i]
                if i==n_row-1:
                    if j % 2 ==0:
                        if len(dat[j])==n_row:
                            result +=dat[j][i]
                if i in range(1,n_row-1):
                    if len(dat[j])>i:
                        result += dat[j][i]
        return result

a=Solution()
lstr="PAYPALISHIRING"
print(a.convert(lstr,7))
            
            