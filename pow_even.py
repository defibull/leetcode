def pow_e(x,n):
        s = x
        while n/2:
            s*=s
            n/=2
        return s
print pow_e(3,4)
