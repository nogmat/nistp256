from math import *

class Curve:

    def __init__(self, p, a, b, G, n):
        self.params = {'p': p, 'a': a, 'b': b, 'G': G, 'n': n}

    def extended_euclidean_algorithm(self, u, v):

        r0, r1 = max(u, v), min(u, v)
        a0, b0 = 1, 0
        a1, b1 = 0, 1
        # Initial step
        q, r2 = r0 // r1, r0 % r1
        a2, b2 = a0 - q*a1, b0 - q*b1
        while r2 > 0:
            a0, b0 = a1, b1
            a1, b1 = a2, b2
            r0 = r1
            r1 = r2
            q, r2 = r0 // r1, r0 % r1
            assert(r0 == q*r1 + r2)
            a2, b2 = a0 - q*a1, b0 - q*b1
        if u > v:
            assert(a1*u+b1*v == 1)
            return a1, b1
        else:
            assert(a1*v+b1*u == 1)
            return b1, a1

    def inverse_finite_field(self, u):
        
        u = u % self.params['p']
        v, k = self.extended_euclidean_algorithm(u, self.params['p'])
        return v

    def pointAdd(self, P, Q):

        x_p, y_p = P
        x_q, y_q = Q

        # Dealing with neutral element
        if x_p == 0 and y_p == 0:
            return x_q, y_q
        if x_q == 0 and y_q == 0:
            return x_p, y_p
        if x_p == x_q and (y_p + y_q) % self.params['p'] == 0:
            return 0, 0
        
        l = (y_q-y_p)*self.inverse_finite_field(x_q-x_p)

        x_r = (l**2 - x_p - x_q)%self.params['p']
        y_r = (l*(x_p-x_r) - y_p)%self.params['p']

        return x_r, y_r

    def pointDouble(self, P):

        x_p, y_p = P
        l = (3*(x_p**2)+self.params['a'])*self.inverse_finite_field(2*y_p)

        x_r = (l**2-x_p-x_p)%self.params['p']
        y_r = (l*(x_p-x_r)-y_p)%self.params['p']

        return x_r, y_r

    def pointMultiplyByScalar(self, P, d_init):

        d = d_init
        Q = 0, 0
        r = d%2
        while d > 0:
            if r == 1:
                if d == d_init:
                    Q = P
                else:
                    Q = self.pointAdd(P, Q)
            P = self.pointDouble(P)
            d = d // 2
            r = d % 2
        return Q


        
