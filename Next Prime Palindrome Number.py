n = int(input())
def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
def is_palin(num):
    t = num
    s = 0
    while(num!=0):
        r = num%10
        s = s*10+r
        num = num//10
    if s==t:
        return True
    else:
        return False
def next_prime_palin(num):
    num = num+1
    while True:
        if is_prime(num) and is_palin(num):
            return num
        num +=1
if n>=10 and n<=10000:
    r = next_prime_palin(n)
    print(r)