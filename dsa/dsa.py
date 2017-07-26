from json import dumps
from gmpy2 import powmod

def DSASign(p,q,g,x,k,m):
    r=powmod(g,k,p)%q
    if r==0:
        return 0
    else:
        s=powmod(k,-1,q)*(int(sha256(m).hexdigest(),16)+x*r)%q
            if s==0:
                return 0
            else:
                return dumps({'r':r,
                             's':s,
                             'm':m})

