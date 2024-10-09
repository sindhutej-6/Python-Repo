n = int(input())
l = []
def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

for i in range(1,n+1):
    if n%i==0:
        if not is_prime(i):
            l.append(i)
print(len(l))