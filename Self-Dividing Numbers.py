n = int(input())
m = int(input())
def is_self(num):
    t = num
    while t > 0:
        d = t%10
        if d == 0 or num%d != 0:
            return False
        t //= 10
    return True
def check(n,m):
    r = []
    for i in range(n,m+1):
        if is_self(i):
            r.append(i)
    for i in r:
        print(i,end = " ")
check(n,m)