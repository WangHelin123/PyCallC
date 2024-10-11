def fibo_py(n):
    a1=1
    a2=1
    out=0
    for i in range(n-2):
        out=a1+a2
        a1=a2
        a2=out
    return out

