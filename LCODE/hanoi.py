def haoni(n,A,B,C):
    if n==1:
        print('Move disk',n,'from',A,'to',C)
    else:
        haoni(n-1,A,C,B)
        print('Move disk',n,'from',A,'to',C)
        haoni(n-1,B,A,C)

n=5
haoni(n,"A","B","C")