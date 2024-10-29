import math
n = int(input())
l = list(map(int,input().split()))
s = math.floor(sum(l)/n)
if s in l:
    print("True")
else:
    print("False")