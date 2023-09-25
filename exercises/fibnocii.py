def fibnocii(n):
    if (n==1)or(n==2):
        return(1)
    else:
        return fibnocii(n-1)+fibnocii(n-2)

for n in range(1,8):
    print(fibnocii(n))

        