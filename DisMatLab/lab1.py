from math import *
import numpy as np
from sympy import symbols, Eq, solve

def lab_main():
    n = -1
    while n < 0:
        n = int(input("Unesite nenegativan cijeli broj: "))
    b = []
    c = []

    for i in range(2):
        for j in range(3):
            if i == 0:
                b.append(int(input("Unesite vrijednost broja b_" + str(j) + ": ")))
            else:
                c.append(int(input("Unesite vrijednost broja c_" + str(j) + ": ")))
    # Optimizitano
    '''
    lam1, lam2 = symbols('lam1 lam2')
    prva_jed = Eq(b[2] - b[1] * lam1 - b[0] * lam2, 0)
    druga_jed = Eq(c[2] - c[1] * lam1 - c[0] * lam2, 0)
    lam = solve((prva_jed, druga_jed), (lam1, lam2))'''

    # Sporije - moj direktan kod
    if b[1] * c[0] - b[0] * c[1] == 0:
        print("Sustav je neodređen")
        return 0;

    lam2 = (c[2] * b[1] - b[2] * c[1]) / (b[1] * c[0] - b[0] * c[1])
    lam1 = (b[2] - lam2 * b[0]) / b[1]

    print(str(lam1) + "  |  " + str(lam2))


   # lam1 = lam2 = -1
    nul_t = np.roots([1, -1*lam1, -1*lam2])
    print(nul_t)

    A, B = symbols('A B')
    if not isinstance(nul_t[0], complex):
        if nul_t[0] != nul_t[1]:
            pr_rek = Eq(b[0]-A - B, 0)
            dr_rek = Eq(b[1] - A * nul_t[0] - B * nul_t[1], 0)
            konst = solve((pr_rek, dr_rek), (A, B))
            A = konst[A]
            B = konst[B]
            print("Vrijednost broja b_n: " + str(int(A*pow(nul_t[0], n) + B*pow(nul_t[1], n))))
        elif nul_t[0] == nul_t[1]:
            pr_rek = Eq(b[0]-A, 0)
            dr_rek = Eq(b[1] - A * nul_t[0] - B * nul_t[1], 0)
            konst = solve((pr_rek, dr_rek), (A, B))
            A = konst[A]
            B = konst[B]
            print("Vrijednost broja b_n: " + str(int(A * pow(nul_t[0], n) + n * B * pow(nul_t[1], n))))
    else:
        x = np.real(nul_t[0])
        y = np.imag(nul_t[0])
        r = sqrt(x**2 + y**2)
        fi = acos(x/r)
        pr_rek = Eq(b[0] - A, 0)
        dr_rek = Eq(b[1] - A * r*cos(fi) - B * r * sin(fi) , 0)
        konst = solve((pr_rek, dr_rek), (A, B))
        A = konst[A]
        B = konst[B]
        print("radius= " +str(r) + " | fi =" + str(fi)+ " | A= " + str(A) + " |B = "+ str(B))

        print("Vrijednost broja b_n: " + str(int(A * pow(r, n)*cos(n*fi) + B * pow(r, n)* sin(n*fi))))



lab_main()
