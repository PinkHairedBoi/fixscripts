from math import*
while True:
    print("Ruudu karakteristikud")
    a = float(input("Sisesta ruudu külje pikkus => "))
    if a<=0:
        print("Vale sisend!")
    else:
        S=a*2
        print("Ruudu pindala", round(S,2))
        P=4*a
        print("Ruudu ümbermõõt", P)
        di=sqrt(a)
        print("Ruudu diagonaal", round(di,2))
    print()
    print("Ristküliku karakteristikud")
    b=float(input("Sisesta ristküliku 1. külje pikkus => "))
    c=float(input("Sisesta ristküliku 2. külje pikkus => "))
    if b<=0 or c<=0:
        print("Vale sisend!")
    else:
        S=b*c
        print("Ristküliku pindala", S)
        P=2(b+c)
        print("Ristküliku ümbermõõt", P)
        di=sqrt(b*2+c*2)
        print("Ristküliku diagonaal", round(di,2))
        print()
    print("Ringi karakteristikud")
    r=float(input("Sisesta ringi raadiuse pikkus => "))
    if r<=0:
        print("Vale sisend!")
    else:
        d=2*r
        print("Ringi läbimõõt", d)
        S=pi*r*2
        print("Ringi pindala", round(S,2))
        C=2*pi*r
        print("Ringjoone pikkus", round(C,2))
        print()
        kysimus=input("Kas arvutan uuesti? Y/N => ")
    if kysimus == "N":
        print("Arvutuste lõpp")
        break
