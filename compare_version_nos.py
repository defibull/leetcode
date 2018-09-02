def compareVersion(A, B):
        a = A.split(".")
        while int(a[len(a)-1]) == 0:
            a = a[:len(a)-1]
        b = B.split(".")
        while int(b[len(b)-1]) == 0:
            b = b[:len(b)-1]
        print a , b
        i = 0
        m = min(len(a), len(b))
        while i < m:
            if int(a[i]) > int(b[i]):
                return 1 # A greater
            elif int(b[i]) > int(a[i]):
                return -1 # B
            else:
                i+=1

        if len(a) > len(b):
            return 1 # A greater
        elif len(b) > len(a):
            return -1 # B greater
        else:
            return 0
print compareVersion("1.0.0.0.0", "1.0")
