from math import *
import numpy as np


def det2x2(mat):
    return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]


def cramer_rule(coef_1a, coef_1b, sol_1, coef_2a, coef_2b, sol_2):  # 2 jed. sa 2 nepoznanice
    det_x = det2x2([[sol_1, coef_1b],  # coef_x[a,b] -> x - broj jed. (ili 1 ili 2)
                    [sol_2, coef_2b]])  # [a,b] -> 1. tj 2. argument u funkciji
    det_y = det2x2([[coef_1a, sol_1],  # sol_x -> slobodni član ("izraz sa desne strane")
                    [coef_2a, sol_2]])
    det_sus = det2x2([[coef_1a, coef_1b],
                      [coef_2a, coef_2b]])
    if det_sus == 0:
        print("Sustav ima beskonačno mnogo ili nema rješenja")
    else:
        return [det_x / det_sus, det_y / det_sus]


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

    # Kramer - sustav 2 jednadžbe sa 2 nepoznanice
    lam1 = cramer_rule(b[1], b[0], b[2], c[1], c[0], c[2])[0]
    lam2 = cramer_rule(b[1], b[0], b[2], c[1], c[0], c[2])[1]
    nul_t = np.roots([1, -1 * lam1, -1 * lam2])

    if not isinstance(nul_t[0], complex):  # korijeni realni
        if nul_t[0] != nul_t[1]:    # korijeni različiti
            # Kramer                                                    bn = A * nt1^n + B * nt2^n
            A = cramer_rule(1, 1, b[0], nul_t[0], nul_t[1], b[1])[0]  # b[0] = A + B
            B = cramer_rule(1, 1, b[0], nul_t[0], nul_t[1], b[1])[1]  # b[1] = A * nt1 + B * nt2
            print("Vrijednost broja b_n: " + str(int(A * pow(nul_t[0], n) + B * pow(nul_t[1], n))))
        elif nul_t[0] == nul_t[1]:  # korijeni isti
            # Kramer                                                    bn = A * nt1^n + B * n * nt2^n ; nt1 = nt2
            A = cramer_rule(1, 0, b[0], nul_t[0], nul_t[1], b[1])[0]  # b[0] = A
            B = cramer_rule(1, 0, b[0], nul_t[0], nul_t[1], b[1])[1]  # b[1] = A * nt1 + B * nt2
            print("Vrijednost broja b_n: " + str(int(A * pow(nul_t[0], n) + n * B * pow(nul_t[1], n))))

    else:       # korijeni kompleksni
        x = np.real(nul_t[0])   # izdvajanje realnog dijela
        y = np.imag(nul_t[0])   # izdvajanje imaginarnog dijela
        r = sqrt(x ** 2 + y ** 2)   # radijus komplx. broja
        fi = acos(x / r)     # kut u radijanima
        # Kramer                                                        bn = A * r^n * cos(fi*n) + B * r^n * sin(fi*n)
        A = cramer_rule(1, 0, b[0], r * cos(fi), r * sin(fi), b[1])[0]  # b[0] = A
        B = cramer_rule(1, 0, b[0], r * cos(fi), r * sin(fi), b[1])[1]  # b[1] = A*r*cos(fi)
        print("Vrijednost broja b_n: " + str(int(A * pow(r, n) * cos(n * fi) + B * pow(r, n) * sin(n * fi))))


lab_main()
