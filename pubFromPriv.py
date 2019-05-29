from point import *
from casting import *
import sys

p = hex2int("FFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF")
a = hex2int("FFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFC")
b = hex2int("5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B")
Gx = hex2int("6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296")
Gy = hex2int("4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5")
n = hex2int("FFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551")


curve = Curve(p,a,b,(Gx,Gy),n)
Gx, Gy = curve.params['G']
G = Gx, Gy

if __name__ == "__main__":
    # Tests
    ## G should be on the curve
    assert((Gy**2 - Gx**3 - a*Gx - b)%p == 0)
    ## n*G should be neutral element over the curve
    O = curve.pointMultiplyByScalar(G, n)
    Ax, Ay = curve.pointAdd(G, O)
    assert(Ax == Gx)
    assert(Ay == Gy)

    privateKey = hex2int(sys.argv[1].upper())
    publicKey = curve.pointMultiplyByScalar(G, privateKey)

    pubX, pubY = publicKey
    pubX, pubY = int2hex(pubX), int2hex(pubY)
    publicKey = "04" + pubX + pubY
    publicKey = publicKey.lower()
    print(publicKey)

    
