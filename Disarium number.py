import math
n = list(map(int,input()))
s = 0
for i in range(len(n)):
    s = s + int(math.pow(n[i],i+1))
x = int(''.join(map(str,n)))
print(x==s)
