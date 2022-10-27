def rekurzija(n, lam1, lam2, arr):
    '''
    :param n: željeni član rekurzivne relacije
    :param lam1: - koef. uz n-1 član relacije
    :param lam2: - koef. uz n-2 član relacije
    :param arr: - osnovni članovi relacije
    :return: n-ti član rekurzivne relacije
    '''

    if n == 0:
        return arr[0]
    elif n == 1:
        return arr[1]
    else:
        return lam1 * rekurzija(n - 1, lam1, lam2, arr) + lam2 * rekurzija(n - 2, lam1, lam2, arr)


def lab_main():
    n = -1
    while (n < 0):
        n = int(input("Unesite nenegativan cijeli broj: "))
    b = []
    c = []

    for i in range(2):
        for j in range(3):
            if i == 0:
                b.append(int(input("Unesite vrijednost broja b_" + str(j) + ": ")))
            else:
                c.append(int(input("Unesite vrijednost broja c_" + str(j) + ": ")))

    lam2 = (c[2] * b[1] - b[2] * c[1]) / (b[1] * c[0] - b[0] * c[1])
    lam1 = (b[2] - lam2 * b[0]) / b[1]
    print("Vrijednost broja b_n: " + str(rekurzija(n, lam1, lam2, b)))


lab_main()
