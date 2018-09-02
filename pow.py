def pow_e(x,n,d):
    s = x
    if n == 0:
        return 1
    while n > 0:
        if s%10 == 0:
            return
        if n%2 == 0:
            s = s*s
            n/=2
        else:
            s = x*s*s
            n = (n-1)/2
    return s
def pow(x, n, d):
        if n%2 == 0:
            p = pow_e(x,n)
        else:
            p = pow_e(x,n-1)
            p*=x
        q = int(p/d)
        low = 0
        high = d
        while low <= high:
            mid = (low+high)/2
            ans = q*d+mid
            if ans == p:
                return mid
            elif ans < p:
                low = mid+1
            else:
                high = mid-1
print pow_e(71045970, 41535484) #, 64735492
