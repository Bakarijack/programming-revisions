#return gcd of two numbers
def gcd(n1,n2):
    gcd = 1  #initial value for gcd
    k = 2   
    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k #update
        k += 1
    return gcd 