import math
def solve(A):
    if A < 2:
        return 1
    else:
        n_ = A
        h_ = int(math.log(n_,2))
        m_ = 2**h_
        p_ = 1+ n_ - 2**h_
        if p_ >= m_/2:
            L_ = (2**h_)-1
        else:
            L_ = (2**h_)-1-((m_/2)-p_)
        f_ = math.factorial
        return (f_(n_-1) / f_(L_) / f_((n_-1)-L_))*solve(L_)*solve(n_-1-L_)
print solve(20)
